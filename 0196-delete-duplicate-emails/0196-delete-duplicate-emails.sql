# Write your MySQL query statement below
DELETE T1 FROM Person T1
INNER JOIN Person T2
WHERE T1.id > T2.id AND T1.email = T2.email;