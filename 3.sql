SELECT e.name,
  c.tax_percentage * p.salary as tax
FROM  employees as e
FULL OUTER JOIN contracts as c ON c.id = e.id
FULL OUTER JOIN positions as p ON p.id = e.id
GROUP BY e.name
WHERE p.salary < 50000


