-- AVG sale price per store
SELECT
	s.store_name, AVG(rd.sale_price) as avg_saleprice
FROM
	raw_deals rd
JOIN
	stores s ON rd.store_id = s.store_id
GROUP BY
	s.store_name
ORDER BY
	avg_saleprice ASC;


-- Store with MOST deals
SELECT 
	s.store_name, COUNT(rd.sale_price) deals
FROM
	raw_deals rd
JOIN
	stores s ON rd.store_id = s.store_id
GROUP BY
	s.store_name
ORDER BY 
	deals DESC
LIMIT 1;

-- Top 10 games with CURRENT biggest discount
WITH cte_discount AS (
SELECT 
	s.store_id,
	s.store_name, 
	rd.deal_id,
	rd.title, 
	ROUND(((rd.original_price - rd.sale_price)/rd.original_price)*100, 2) as discount_percent,
	rd.fetched_at
FROM 
	raw_deals rd
JOIN
	stores s ON rd.store_id = s.store_id
WHERE 
	fetched_at = (SELECT MAX(fetched_at) FROM raw_deals)
)
SELECT 
	store_name,
	title,
	discount_percent
FROM cte_discount
ORDER BY 
	cte_discount.discount_percent DESC
LIMIT 10;

-- COUNT of games seen across stores (Availibility)
WITH cte_lol AS (
SELECT 
	rd.title,
	rd.store_id
FROM 
	raw_deals rd
GROUP BY 
	rd.title,rd.store_id
ORDER BY 
	title
)
SELECT 
	title, 
	COUNT(title) appearances
FROM 
	cte_lol
GROUP BY 
	title
ORDER BY 
	appearances DESC

-- Full price history for each game
SELECT 
	rd.title, 
	s.store_name,
	rd.sale_price,
	LAG(rd.sale_price) OVER (PARTITION BY rd.store_id ORDER BY rd.fetched_at) as prev_price,
	rd.sale_price - LAG(rd.sale_price) OVER (PARTITION BY rd.store_id ORDER BY rd.fetched_at) as price_difference
FROM 
	raw_deals rd
JOIN 
	stores s ON rd.store_id = s.store_id
ORDER BY 
	fetched_at DESC;