# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 11:31:38 2025

@author: PC
"""

# Filter large orders
def flag_large_orders(orders, products):
    large_orders = []
    for order in orders:
        product_id = order['product_id']
        price = products[product_id]['price']
        if price * order['quantity'] > 100:
            large_orders.append(order)
    return large_orders

# Convert price from NGN to USD
def convert_prices(products, rate=0.000667):  # NGN to USD
    return {pid: {'name': p['product_name'], 'price': p['price'] * rate} for pid, p in products.items()}