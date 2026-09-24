SELECT 
	rd.title, 
	rd.fetched_at, 
	rd.sale_price, 
	s.store_name,
	rd.sale_price - LAG(rd.sale_price) OVER (PARTITION BY rd.store_id ORDER BY rd.fetched_at) as price_difference
FROM 
	raw_deals rd
JOIN 
	stores s ON rd.store_id = s.store_id
WHERE 
	title = 'The Incredible Adventures of Van Helsing Anthology'
ORDER BY fetched_at;