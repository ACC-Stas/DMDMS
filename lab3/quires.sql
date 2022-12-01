SELECT MAX(cost) max, AVG(cost) avg, MIN(cost) min FROM Invoice;

SELECT COUNT(*) FROM Contact c WHERE c.email REGEXP '^.+@mail.ru$';

SELECT COUNT(*) FROM Contact c WHERE c.email LIKE '%@mail.ru';

SELECT *
FROM Invoice
WHERE cost > (SELECT AVG(cost) FROM Invoice);

SELECT city FROM Address a ORDER BY a.home DESC, a.id ASC LIMIT 5 OFFSET 2;

