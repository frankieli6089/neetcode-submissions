-- Write your query below
SELECT c.customer_id, customer_name
FROM customers as c
WHERE c.customer_id IN (SELECT o.customer_id
        FROM orders as o
         WHERE o.product_name = 'A')
AND c.customer_id IN (SELECT o.customer_id
        FROM orders as o
         WHERE o.product_name = 'B')
AND c.customer_id NOT IN (SELECT o.customer_id
        FROM orders as o
         WHERE o.product_name = 'C')
ORDER BY c.customer_name
    