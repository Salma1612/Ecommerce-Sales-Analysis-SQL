-- queries.sql
-- SQL + Business Analytics: E-Commerce Sales Analysis
-- Demonstrates: JOIN, GROUP BY, aggregation, and window functions (RANK, LAG)

-- 1. Monthly revenue trend
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(revenue), 2) AS monthly_revenue,
    COUNT(DISTINCT order_id) AS num_orders
FROM orders
GROUP BY month
ORDER BY month;

-- 2. Month-over-month revenue growth (window function: LAG)
WITH monthly AS (
    SELECT
        strftime('%Y-%m', order_date) AS month,
        SUM(revenue) AS monthly_revenue
    FROM orders
    GROUP BY month
)
SELECT
    month,
    ROUND(monthly_revenue, 2) AS monthly_revenue,
    ROUND(
        (monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY month))
        * 100.0 / LAG(monthly_revenue) OVER (ORDER BY month), 2
    ) AS mom_growth_pct
FROM monthly
ORDER BY month;

-- 3. Top 10 customers by total spend (JOIN + window function: RANK)
SELECT
    RANK() OVER (ORDER BY SUM(o.revenue) DESC) AS spend_rank,
    c.customer_id,
    c.region,
    ROUND(SUM(o.revenue), 2) AS total_spend,
    COUNT(o.order_id) AS num_orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.region
ORDER BY total_spend DESC
LIMIT 10;

-- 4. Category-wise revenue share (GROUP BY + aggregate %)
SELECT
    category,
    ROUND(SUM(revenue), 2) AS category_revenue,
    ROUND(SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM orders), 2) AS pct_of_total_revenue,
    COUNT(order_id) AS num_orders
FROM orders
GROUP BY category
ORDER BY category_revenue DESC;

-- 5. Revenue by region (JOIN + GROUP BY)
SELECT
    c.region,
    ROUND(SUM(o.revenue), 2) AS region_revenue,
    COUNT(DISTINCT o.customer_id) AS active_customers,
    ROUND(SUM(o.revenue) / COUNT(DISTINCT o.customer_id), 2) AS revenue_per_customer
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY region_revenue DESC;
