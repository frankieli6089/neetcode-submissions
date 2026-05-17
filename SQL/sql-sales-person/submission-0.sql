-- Write your query below
SELECT sp.name
FROM sales_person as sp
WHERE NOT EXISTS (SELECT sp.name
                FROM orders as o, company as c
                WHERE sp.sales_id = o.sales_id
                AND c.com_id = o.com_id
                AND c.name = 'CRIMSON'
                )