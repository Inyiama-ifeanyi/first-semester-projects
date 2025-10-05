SELECT * FROM customers;
SELECT * FROM products WHERE category = 'Drinks';
SELECT * FROM orders ORDER BY order_date DESC;

SELECT COUNT(*) FROM orders;
SELECT product_id, SUM(price * quantity) AS revenue
FROM orders JOIN products USING (product_id)
GROUP BY product_id;
SELECT AVG(price) FROM products;

SELECT o.order_id, c.name, p.product_name, o.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;
SELECT c.name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;