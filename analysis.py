"""
analysis.py
-----------
Runs the SQL queries in queries.sql against ecommerce.db, prints results,
and generates two charts (monthly revenue trend, category revenue share)
for the README / report.
"""

import sqlite3
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

conn = sqlite3.connect("ecommerce.db")

# 1. Monthly revenue trend
monthly_revenue = pd.read_sql_query("""
    SELECT strftime('%Y-%m', order_date) AS month,
           ROUND(SUM(revenue), 2) AS monthly_revenue,
           COUNT(DISTINCT order_id) AS num_orders
    FROM orders
    GROUP BY month
    ORDER BY month
""", conn)
print("\n=== Monthly Revenue Trend ===")
print(monthly_revenue.to_string(index=False))

# 2. Month-over-month growth
mom_growth = pd.read_sql_query("""
    WITH monthly AS (
        SELECT strftime('%Y-%m', order_date) AS month, SUM(revenue) AS monthly_revenue
        FROM orders GROUP BY month
    )
    SELECT month, ROUND(monthly_revenue, 2) AS monthly_revenue,
           ROUND((monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY month)) * 100.0
                 / LAG(monthly_revenue) OVER (ORDER BY month), 2) AS mom_growth_pct
    FROM monthly ORDER BY month
""", conn)
print("\n=== Month-over-Month Growth % ===")
print(mom_growth.to_string(index=False))

# 3. Top 10 customers by spend
top_customers = pd.read_sql_query("""
    SELECT RANK() OVER (ORDER BY SUM(o.revenue) DESC) AS spend_rank,
           c.customer_id, c.region,
           ROUND(SUM(o.revenue), 2) AS total_spend,
           COUNT(o.order_id) AS num_orders
    FROM orders o JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.region
    ORDER BY total_spend DESC LIMIT 10
""", conn)
print("\n=== Top 10 Customers by Spend ===")
print(top_customers.to_string(index=False))

# 4. Category revenue share
category_revenue = pd.read_sql_query("""
    SELECT category, ROUND(SUM(revenue), 2) AS category_revenue,
           ROUND(SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM orders), 2) AS pct_of_total_revenue,
           COUNT(order_id) AS num_orders
    FROM orders GROUP BY category ORDER BY category_revenue DESC
""", conn)
print("\n=== Category-wise Revenue Share ===")
print(category_revenue.to_string(index=False))

# 5. Revenue by region
region_revenue = pd.read_sql_query("""
    SELECT c.region, ROUND(SUM(o.revenue), 2) AS region_revenue,
           COUNT(DISTINCT o.customer_id) AS active_customers,
           ROUND(SUM(o.revenue) / COUNT(DISTINCT o.customer_id), 2) AS revenue_per_customer
    FROM orders o JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.region ORDER BY region_revenue DESC
""", conn)
print("\n=== Revenue by Region ===")
print(region_revenue.to_string(index=False))

# --- Charts ---
plt.figure(figsize=(8, 4.5))
plt.plot(monthly_revenue["month"], monthly_revenue["monthly_revenue"], marker="o")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Revenue")
plt.title("Monthly Revenue Trend")
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 5))
plt.pie(category_revenue["category_revenue"], labels=category_revenue["category"],
        autopct="%1.1f%%", startangle=90)
plt.title("Revenue Share by Category")
plt.tight_layout()
plt.savefig("category_revenue_share.png", dpi=150)
plt.close()

print("\nSaved monthly_revenue_trend.png and category_revenue_share.png")

# --- Key business takeaways (derived directly from the above outputs) ---
top_category = category_revenue.iloc[0]
top_region = region_revenue.iloc[0]
best_month = monthly_revenue.loc[monthly_revenue["monthly_revenue"].idxmax()]
avg_growth = mom_growth["mom_growth_pct"].dropna().mean()

print("\n=== Key Takeaways ===")
print(f"1. {top_category['category']} is the top revenue category at "
      f"{top_category['pct_of_total_revenue']}% of total revenue.")
print(f"2. {top_region['region']} region generates the highest total revenue "
      f"(₹{top_region['region_revenue']:,.2f}), with ₹{top_region['revenue_per_customer']:,.2f} revenue per active customer.")
print(f"3. Peak month: {best_month['month']} with ₹{best_month['monthly_revenue']:,.2f} revenue.")
print(f"4. Average month-over-month growth: {avg_growth:.2f}%.")

conn.close()
