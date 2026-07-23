import requests
import filter_deals as fd
import save_deals as sd

url = "https://www.cheapshark.com/api/1.0/deals"

query_params = {
    "upperPrice": 15
}

header = {
    "User-Agent": "MyGameDealFinderApp/1.0"
}

response = requests.get(url, headers=header, params=query_params)

found_deals = False
# Collects data from url, only if it was a success (status code: 200)
def collect_data():
    if response.status_code == 200:
        data = response.json()
        print(f"Found {len(data)} Deals!")
        return data
    else:
        print(f"Error, Status code: {response.status_code}", response.text)

# Normalizes the data to fit custom headers
def normalize_deals(deals):
    if deals:
        normalized = [{"title": deal["title"], "original_price": float(deal["normalPrice"]), "sale_price": float(deal["salePrice"]), "store": deal["storeID"]} for deal in deals]
        return normalized

if __name__ == "__main__":
    deals = collect_data()

    sd.write_raw_json('data/raw/raw_deals.json', deals)
    filtered = fd.filter_discount(50, normalize_deals(deals))
    print(filtered)

