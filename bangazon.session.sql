/*
 To compare user's id, with their customer id's.
 */
SELECT au.id AS user_id,
 c.id AS cust_id,
 at.key,
 username,
 first_name || " " || last_name
FROM auth_user au
 INNER JOIN authtoken_token at ON au.id = at.user_id
 INNER JOIN bangazonapi_customer c ON au.id = c.user_id;
/*
 To compare user ratings for products.
 */
SELECT p.id AS product_id,
 p.name AS product_name,
 p.price,
 p.description,
 p.quantity,
 p.customer_id,
 r.rating,
 r.product_id
FROM bangazonapi_product p
 INNER JOIN bangazonapi_productrating r ON p.customer_id = r.customer_id
ORDER BY p.customer_id;
/*
 Confirm creating of products under 10000.
 Where the last 5 or products from location NSS were created to verfify products can be
 created with price over 10000.
 */
SELECT *
FROM bangazonapi_product
ORDER BY price DESC
LIMIT 5;

SELECT p.id,
 p.name,
 p.price,
 p.description,
 p.quantity
FROM bangazonapi_product p
WHERE price <= 999
ORDER BY price DESC;
