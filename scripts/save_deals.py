import csv
import filter_deals as fd



fields = ["title", "original_price", "sale_price", "store"]

def write_games(filepath, discount_threshold):
    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(fd.filter_discount(discount_threshold))

write_games('data/processed/top_deals.csv', 50)