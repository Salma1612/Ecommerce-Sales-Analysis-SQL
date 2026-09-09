"""
generate_data.py
-----------------
Generates a realistic SYNTHETIC e-commerce transactions dataset for the
SQL + Business Analytics project. Data is randomly generated (seeded for
reproducibility) with realistic seasonal patterns, categories, and
customer segments -- it is not scraped or copied from any real company's
data. Clearly labeled as synthetic in the README.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

N_CUSTOMERS = 400
N_ORDERS = 6000
START_DATE = datetime(2025, 9, 1)
END_DATE = datetime(2026, 8, 31)

CATEGORIES = {
    "Electronics": (1500, 45000),
    "Home & Kitchen": (300, 8000),
    "Fashion": (400, 5000),
    "Books": (150, 1200),
    "Sports & Fitness": (500, 12000),
    "Beauty & Personal Care": (200, 3500),
}

REGIONS = ["North", "South", "East", "West", "Central"]

# --- Customers ---
customer_ids = [f"CUST{str(i).zfill(4)}" for i in range(1, N_CUSTOMERS + 1)]
signup_dates = [
    START_DATE - timedelta(days=int(np.random.exponential(200)))
    for _ in range(N_CUSTOMERS)
]
customers = pd.DataFrame({
    "customer_id": customer_ids,
    "region": np.random.choice(REGIONS, N_CUSTOMERS, p=[0.25, 0.2, 0.2, 0.2, 0.15]),
    "signup_date": signup_dates,
})
customers.to_csv("customers.csv", index=False)

# --- Orders (with seasonal + weekend effects) ---
def random_date_with_seasonality():
    total_days = (END_DATE - START_DATE).days
    day_offset = np.random.randint(0, total_days)
    date = START_DATE + timedelta(days=day_offset)
    return date

rows = []
order_id = 1
for _ in range(N_ORDERS):
    date = random_date_with_seasonality()

    # Seasonal boost: Nov-Dec (festive/holiday season) get more orders
    if date.month in (11, 12):
        if np.random.rand() < 0.4:
            continue  # skip to effectively oversample later via duplication below

    category = np.random.choice(list(CATEGORIES.keys()), p=[0.22, 0.18, 0.22, 0.10, 0.16, 0.12])
    price_range = CATEGORIES[category]
    unit_price = round(np.random.uniform(*price_range), 2)
    quantity = np.random.choice([1, 1, 1, 2, 2, 3], p=[0.45, 0.2, 0.15, 0.1, 0.05, 0.05])
    customer_id = np.random.choice(customer_ids)

    rows.append({
        "order_id": f"ORD{str(order_id).zfill(5)}",
        "customer_id": customer_id,
        "order_date": date.strftime("%Y-%m-%d"),
        "category": category,
        "quantity": quantity,
        "unit_price": unit_price,
        "revenue": round(quantity * unit_price, 2),
    })
    order_id += 1

# Oversample Nov/Dec to simulate a real festive-season demand spike
festive_boost = []
for _ in range(int(N_ORDERS * 0.18)):
    date = datetime(2025, 11, 1) + timedelta(days=np.random.randint(0, 60))
    category = np.random.choice(list(CATEGORIES.keys()), p=[0.28, 0.15, 0.25, 0.08, 0.14, 0.10])
    price_range = CATEGORIES[category]
    unit_price = round(np.random.uniform(*price_range), 2)
    quantity = np.random.choice([1, 1, 2, 2, 3], p=[0.4, 0.25, 0.15, 0.1, 0.1])
    customer_id = np.random.choice(customer_ids)
    festive_boost.append({
        "order_id": f"ORD{str(order_id).zfill(5)}",
        "customer_id": customer_id,
        "order_date": date.strftime("%Y-%m-%d"),
        "category": category,
        "quantity": quantity,
        "unit_price": unit_price,
        "revenue": round(quantity * unit_price, 2),
    })
    order_id += 1

orders = pd.DataFrame(rows + festive_boost)
orders = orders.sort_values("order_date").reset_index(drop=True)
orders.to_csv("orders.csv", index=False)

print(f"Generated {len(customers)} customers and {len(orders)} orders")
print(f"Date range: {orders['order_date'].min()} to {orders['order_date'].max()}")
print(f"Total revenue: {orders['revenue'].sum():,.2f}")
