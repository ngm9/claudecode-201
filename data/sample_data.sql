-- ShopFlow Sample Data

-- Categories
INSERT INTO categories (id, name, parent_id) VALUES
(1, 'Electronics', NULL),
(2, 'Clothing', NULL),
(3, 'Home & Kitchen', NULL),
(4, 'Sports', NULL),
(5, 'Books', NULL);

-- Suppliers
INSERT INTO suppliers (id, name, rating) VALUES
(1, 'TechSupply Co', 5),
(2, 'FashionWholesale', 4),
(3, 'HomeGoods Inc', 3);

-- Warehouses
INSERT INTO warehouses (id, name, location) VALUES
(1, 'Mumbai Central', 'Mumbai, Maharashtra'),
(2, 'Bangalore Tech Park', 'Bangalore, Karnataka'),
(3, 'Delhi NCR Hub', 'Gurugram, Haryana');

-- Products
INSERT INTO products (id, name, description, base_price, category_id, supplier_id) VALUES
(1, 'Wireless Bluetooth Headphones', 'Over-ear noise cancelling headphones', 2499.00, 1, 1),
(2, 'USB-C Charging Cable', '2m braided fast-charge cable', 399.00, 1, 1),
(3, 'Mechanical Keyboard', 'RGB backlit with Cherry MX switches', 4999.00, 1, 1),
(4, 'Cotton Crew T-Shirt', '100% cotton, unisex fit', 599.00, 2, 2),
(5, 'Denim Jeans Slim Fit', 'Stretchable slim fit jeans', 1299.00, 2, 2),
(6, 'Running Shoes', 'Lightweight mesh running shoes', 2199.00, 4, 2),
(7, 'Stainless Steel Water Bottle', '1L insulated bottle', 799.00, 3, 3),
(8, 'Non-Stick Frying Pan', '26cm ceramic coated pan', 1199.00, 3, 3),
(9, 'Yoga Mat', '6mm thick anti-slip mat', 899.00, 4, 3),
(10, 'The Pragmatic Programmer', 'Classic software engineering book', 650.00, 5, 3),
(11, 'Laptop Stand', 'Adjustable aluminum laptop stand', 1899.00, 1, 1),
(12, 'Resistance Bands Set', 'Set of 5 with carrying bag', 499.00, 4, 2);

-- Inventory (some deliberately below reorder_level for low_stock exercise)
INSERT INTO inventory (product_id, warehouse_id, quantity, reorder_level) VALUES
(1, 1, 45, 10),
(1, 2, 3, 10),     -- LOW STOCK
(2, 1, 200, 50),
(2, 3, 15, 50),    -- LOW STOCK
(3, 2, 8, 10),     -- LOW STOCK
(4, 1, 120, 20),
(4, 3, 5, 20),     -- LOW STOCK
(5, 1, 60, 15),
(5, 2, 25, 15),
(6, 2, 2, 10),     -- LOW STOCK
(6, 3, 18, 10),
(7, 1, 90, 20),
(7, 3, 7, 20),     -- LOW STOCK
(8, 1, 35, 10),
(9, 2, 4, 10),     -- LOW STOCK
(9, 3, 22, 10),
(10, 1, 50, 10),
(10, 3, 12, 10),
(11, 2, 6, 10),    -- LOW STOCK
(12, 1, 75, 15),
(12, 3, 9, 15);    -- LOW STOCK

-- Sample inventory movements
INSERT INTO inventory_movements (product_id, warehouse_id, movement_type, quantity_delta, reference, notes, user_name) VALUES
(1, 1, 'in', 50, 'PO-2024-001', 'Initial stock from TechSupply Co', 'admin'),
(1, 1, 'out', -5, 'ORD-2024-101', 'Sold via online store', 'system'),
(2, 1, 'in', 200, 'PO-2024-002', 'Bulk cable order', 'admin'),
(4, 1, 'in', 150, 'PO-2024-003', 'Seasonal restock', 'admin'),
(4, 1, 'out', -30, 'ORD-2024-105', 'Corporate bulk order', 'system'),
(6, 2, 'in', 10, 'PO-2024-004', 'New shoe model arrival', 'admin'),
(6, 2, 'out', -8, 'ORD-2024-110', 'Flash sale orders', 'system');

-- Reset sequences to avoid conflicts with future inserts
SELECT setval('categories_id_seq', (SELECT MAX(id) FROM categories));
SELECT setval('suppliers_id_seq', (SELECT MAX(id) FROM suppliers));
SELECT setval('warehouses_id_seq', (SELECT MAX(id) FROM warehouses));
SELECT setval('products_id_seq', (SELECT MAX(id) FROM products));
SELECT setval('inventory_id_seq', (SELECT MAX(id) FROM inventory));
SELECT setval('inventory_movements_id_seq', (SELECT MAX(id) FROM inventory_movements));
