CREATE TABLE stores(
 store_id INT PRIMARY KEY, 
store_name TEXT 
);

CREATE TABLE raw_deals(
deal_id SERIAL PRIMARY KEY,
store_id INT,
FOREIGN KEY(store_id) REFERENCES stores(store_id),
title TEXT,
original_price NUMERIC,
sale_price NUMERIC,
fetched_at TIMESTAMP
);

CREATE TABLE avg_storeprice(
store_id INT primary key,
store_name text, 
avg_saleprice numeric,
fetched_at timestamp
);

CREATE TABLE top_discounts(
store_id INT,
store_name text, 
deal_id INT primary key,
title text,
discount_percent numeric,
fetched_at timestamp
);

ALTER TABLE raw_deals
ADD CONSTRAINT uq_deal_store_price UNIQUE (title, store_id, sale_price);