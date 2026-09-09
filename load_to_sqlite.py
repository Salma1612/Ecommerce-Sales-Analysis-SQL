"""
load_to_sqlite.py
------------------
Loads customers.csv and orders.csv into a SQLite database (ecommerce.db)
for SQL analysis.
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

customers.to_sql("customers", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

conn.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id)")
conn.execute("CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date)")
conn.commit()

print("Loaded tables: customers, orders into ecommerce.db")
print(f"customers: {len(customers)} rows")
print(f"orders: {len(orders)} rows")

conn.close()
