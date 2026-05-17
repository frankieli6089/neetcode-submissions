-- Write your query below
SELECT e.left_operand,
       e.operator,
       e.right_operand,
       CASE
       WHEN e.operator = '>' AND v.value > v2.value THEN 'true'
       WHEN e.operator = '<' AND v.value < v2.value THEN 'true'
       WHEN e.operator = '=' AND v.value = v2.value THEN 'true'
       ELSE 'false'
    END as value
FROM expressions as e, variables as v, variables as v2
WHERE e.left_operand = v.name
AND e.right_operand = v2.name