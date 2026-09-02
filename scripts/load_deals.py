import fetch_prices as fp
from fetch_prices import collect_data, normalize_deals
import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

deals = normalize_deals(collect_data())

def include_timestamp():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [{**item, 'fetched_at': current_time} for item in deals]

data_to_insert = [(d["title"], d["original_price"], d["sale_price"], int(d["store"]), d["fetched_at"]) for d in include_timestamp()]

def insert_deals():
    with psycopg2.connect(
        dbname="gaming_price_intelligence",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    ) as conn:
        with conn.cursor() as cursor:
            insert_query = "INSERT INTO raw_deals (title, original_price, sale_price, store_id, fetched_at) VALUES %s"

            execute_values(cursor, insert_query, data_to_insert, template="(%s, %s, %s, %s, %s)")
            
insert_deals()

