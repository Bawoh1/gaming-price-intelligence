import csv
import json
import filter_deals as fd
import read_games as rg



fields = ["title", "original_price", "sale_price", "store"]

def write_games(filepath, source):
    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(source)

def write_raw_json(filepath, data):
    with open(filepath, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

write_games('data/processed/top_deals.csv', rg.sample)