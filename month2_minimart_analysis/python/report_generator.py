# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 11:02:07 2025

@author: PC
"""

def generate_report(orders, products):
    # Total products sold
    total_sold = sum(order["quantity"] for order in orders)
    
    # Most popular product
    product_quantities = {}
    for order in orders:
        product_id = order["product_id"]
        quantity = order["quantity"]
        product_quantities[product_id] = product_quantities.get(product_id, 0) + quantity
    most_popular = None
    if product_quantities:
        max_product_id = max(product_quantities, key=product_quantities.get)
        most_popular = products[max_product_id]["product_name"]
    
    # Revenue per customer
    revenue_per_customer = {}
    for order in orders:
        customer_id = order["customer_id"]
        product_id = order["product_id"]
        quantity = order["quantity"]
        price = products[product_id]["price"]
        revenue = price * quantity
        revenue_per_customer[customer_id] = revenue_per_customer.get(customer_id, 0) + revenue
    return {
        "total_products_sold": total_sold,
        "most_popular_product": None,  # Replace
        "revenue_per_customer": {}     # Replace
    }
