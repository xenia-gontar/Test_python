SELECT e.name,
  c.tax_percentage * p.salary as tax
FROM  employees as e
FULL OUTER JOIN contracts as c ON c.id = e.contract_id
FULL OUTER JOIN positions as p ON p.id = e.position_id
WHERE p.salary < 50000


