# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 08:24:01 2025

@author: PC
"""

import psycopg2
from generate_report import generate_report 
from utils import flag_large_orders, convert_prices

def load_sql_data():
    try:
        conn = psycopg2.connect(dbname="minimart_sales_system", user="postgres", password="postgres")
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, customer_id, product_id, quantity, order_date FROM orders")
        orders = [{"order_id": o[0], "customer_id": o[1], "product_id": o[2], "quantity": o[3], "order_date": str(o[4])} for o in cursor.fetchall()]
        cursor.execute("SELECT product_id, product_name, category, price FROM products")
        products = {p[0]: {"product_name": p[1], "category": p[2], "price": p[3]} for p in cursor.fetchall()}
        conn.close()
        return orders, products
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return [], {}

def main():
    orders, products = load_sql_data()
    if not orders or not products:
        print("Failed to load data")
        return
    report = generate_report(orders, products)
    print("Report:", report)
    large_orders = flag_large_orders(orders, products)
    print("Large Orders:", large_orders)
    converted_products = convert_prices(products)
    print("Converted Prices (USD):", converted_products)

if __name__ == "__main__":
    main()