SELECT seller_name
FROM seller as s
WHERE NOT EXISTS (SELECT o.seller_id 
                    FROM orders as o
                    WHERE sale_date >= '2020-01-01' 
                    AND sale_date <= '2020-12-31'
                    AND o.seller_id = s.seller_id)
ORDER BY s.seller_name ASC