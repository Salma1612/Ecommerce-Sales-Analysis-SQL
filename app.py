"""
app.py
------
Interactive Streamlit dashboard for the E-Commerce Sales & Customer
Analysis project. Runs the same SQL queries as analysis.py, but adds
sidebar filters (region, category, date range) for interactive exploration.

Deploy this on Streamlit Community Cloud (share.streamlit.io) by pointing
it at this file as the "main file path" for the repo.
"""

import os
import sqlite3

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="E-Commerce Sales & Customer Analysis",
    page_icon="📊",
    layout="wide",
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))


@st.cache_data
def load_data():
    customers_path = os.path.join(DATA_DIR, "customers.csv")
    orders_path = os.path.join(DATA_DIR, "orders.csv")

    # If the CSVs aren't present in the repo (e.g. fresh clone without data
    # files committed), generate them on the fly so the app still works.
    if not (os.path.exists(customers_path) and os.path.exists(orders_path)):
        import generate_data  # noqa: F401  (runs the generation script as a side effect)

    customers = pd.read_csv(customers_path, parse_dates=["signup_date"])
    orders = pd.read_csv(orders_path, parse_dates=["order_date"])
    return customers, orders


customers, orders = load_data()

# ---------------- Sidebar filters ----------------
st.sidebar.header("Filters")

min_date = orders["order_date"].min().date()
max_date = orders["order_date"].max().date()
date_range = st.sidebar.date_input(
    "Order date range", value=(min_date, max_date), min_value=min_date, max_value=max_date
)

all_regions = sorted(customers["region"].unique())
selected_regions = st.sidebar.multiselect("Region", all_regions, default=all_regions)

all_categories = sorted(orders["category"].unique())
selected_categories = st.sidebar.multiselect("Category", all_categories, default=all_categories)

# ---------------- Apply filters ----------------
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

merged = orders.merge(customers, on="customer_id")
mask = (
    (merged["order_date"].dt.date >= start_date)
    & (merged["order_date"].dt.date <= end_date)
    & (merged["region"].isin(selected_regions))
    & (merged["category"].isin(selected_categories))
)
filtered = merged[mask].copy()

# Build an in-memory SQLite DB from the FILTERED data so all analysis
# below reflects the sidebar selections.
conn = sqlite3.connect(":memory:")
filtered.to_sql("orders", conn, index=False, if_exists="replace")
customers.to_sql("customers", conn, index=False, if_exists="replace")

# ---------------- Header ----------------
st.title("📊 E-Commerce Sales & Customer Analysis")
st.caption(
    "SQL-based revenue, customer, and category analysis on a synthetically generated "
    "e-commerce dataset. Built with Python, SQL (SQLite), and Streamlit. "
    "Use the sidebar to filter by date range, region, and category."
)

if filtered.empty:
    st.warning("No orders match the current filters. Try widening your selection.")
    st.stop()

# ---------------- KPI row ----------------
total_revenue = filtered["revenue"].sum()
total_orders = filtered["order_id"].nunique()
total_customers = filtered["customer_id"].nunique()
avg_order_value = total_revenue / total_orders if total_orders else 0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
k2.metric("Total Orders", f"{total_orders:,}")
k3.metric("Active Customers", f"{total_customers:,}")
k4.metric("Avg Order Value", f"₹{avg_order_value:,.0f}")

st.divider()

# ---------------- Monthly revenue trend ----------------
st.subheader("Monthly Revenue Trend")
monthly = pd.read_sql_query(
    """
    SELECT strftime('%Y-%m', order_date) AS month,
           ROUND(SUM(revenue), 2) AS monthly_revenue
    FROM orders
    GROUP BY month
    ORDER BY month
    """,
    conn,
)
st.line_chart(monthly.set_index("month")["monthly_revenue"])

with st.expander("Month-over-Month Growth % (window function: LAG)"):
    mom = pd.read_sql_query(
        """
        WITH monthly AS (
            SELECT strftime('%Y-%m', order_date) AS month, SUM(revenue) AS monthly_revenue
            FROM orders GROUP BY month
        )
        SELECT month, ROUND(monthly_revenue, 2) AS monthly_revenue,
               ROUND((monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY month)) * 100.0
                     / LAG(monthly_revenue) OVER (ORDER BY month), 2) AS mom_growth_pct
        FROM monthly ORDER BY month
        """,
        conn,
    )
    st.dataframe(mom, use_container_width=True)

st.divider()

# ---------------- Category + Region ----------------
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Revenue Share by Category")
    category_revenue = pd.read_sql_query(
        """
        SELECT category, ROUND(SUM(revenue), 2) AS category_revenue,
               ROUND(SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM orders), 2) AS pct_of_total
        FROM orders GROUP BY category ORDER BY category_revenue DESC
        """,
        conn,
    )
    fig, ax = plt.subplots()
    ax.pie(
        category_revenue["category_revenue"],
        labels=category_revenue["category"],
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.axis("equal")
    st.pyplot(fig)

with col_b:
    st.subheader("Revenue by Region (JOIN + GROUP BY)")
    region_revenue = pd.read_sql_query(
        """
        SELECT c.region,
               ROUND(SUM(o.revenue), 2) AS region_revenue,
               COUNT(DISTINCT o.customer_id) AS active_customers,
               ROUND(SUM(o.revenue) / COUNT(DISTINCT o.customer_id), 2) AS revenue_per_customer
        FROM orders o JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY c.region ORDER BY region_revenue DESC
        """,
        conn,
    )
    st.bar_chart(region_revenue.set_index("region")["region_revenue"])
    st.dataframe(region_revenue, use_container_width=True)

st.divider()

# ---------------- Top customers ----------------
st.subheader("Top 10 Customers by Spend (RANK window function)")
top_customers = pd.read_sql_query(
    """
    SELECT RANK() OVER (ORDER BY SUM(o.revenue) DESC) AS spend_rank,
           c.customer_id, c.region,
           ROUND(SUM(o.revenue), 2) AS total_spend,
           COUNT(o.order_id) AS num_orders
    FROM orders o JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.region
    ORDER BY total_spend DESC LIMIT 10
    """,
    conn,
)
st.dataframe(top_customers, use_container_width=True)

st.divider()
st.caption(
    "Dataset is synthetically generated (seeded, reproducible) for demonstration "
    "purposes — see README.md for details. Source: github.com/Salma1612/Ecommerce-Sales-Analysis-SQL"
)

conn.close()
