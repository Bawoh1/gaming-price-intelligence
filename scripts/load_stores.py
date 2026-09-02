import requests
import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://www.cheapshark.com/api/1.0/stores"

header = {
    "User-Agent": "MyGameDealFinderApp/1.0"
}

response = requests.get(url, headers=header)

def collect_stores():
    if response.status_code == 200:
        data = response.json()
        print(f"Found {len(data)} Stores!")
        return data
    else:
        print(f"Error, Status code: {response.status_code}", response.text)

def normalize_stores(stores):
    if stores:
        normalized = [{"store_id": int(d["storeID"]), "store_name": d["storeName"]} for d in stores]
        return normalized

stores_to_insert = normalize_stores(collect_stores())

def insert_stores():
    with psycopg2.connect(
        dbname="gaming_price_intelligence",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    ) as conn:
        with conn.cursor() as cursor:
            insert_query = "INSERT INTO stores (store_id, store_name) VALUES %s"

            execute_values(cursor, insert_query, stores_to_insert, template="(%(store_id)s, %(store_name)s)")

insert_stores()
