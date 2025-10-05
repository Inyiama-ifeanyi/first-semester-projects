INSERT INTO customers (customer_id, name, email, join_date)
VALUES
	(1, 'Ifeanyi Inyiama', 'inyiamaifeanyi@gmail.com', '2024-04-20'),
	(2, 'Mubby Sani', 'mubbysani@gmail.com', '2020-09-05'),
	(3, 'Tabitha Kavyu', 'tabbykavyu@gmail.com', '2020-12-25'),
	(4, 'Jerry Uke', 'ukejerry@gmail.com', '2020-06-01'),
	(5, 'Confidence Orji', 'confyorji@gmail.com', '2021-04-03');

INSERT INTO products (product_id, product_name, category, price)
VALUES
	(1, 'Cola 500ml', 'Drinks', 500),
    (2, 'Whole Wheat Bread', 'Bakery', 1200),
    (3, 'Apples (1kg)', 'Produce', 2500),
    (4, 'Toothpaste', 'Personal Care', 750),
    (5, 'Tissue Paper', 'Household', 300);

INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date)
VALUES
	(1, 1, 1, 2, '2025-06-01'),
	(2, 2, 3, 1, '2025-06-02'),
    (3, 3, 2, 3, '2025-06-03'), 
    (4, 4, 4, 1, '2025-06-04'), 
    (5, 1, 5, 4, '2025-06-05');