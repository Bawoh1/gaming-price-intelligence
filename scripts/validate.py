from fetch_prices import collect_data, normalize_deals
deals = normalize_deals(collect_data())

def needs_validation(deals):
    needs_valid = [d for d in deals if d['sale_price'] == 0.00]

    for deal in needs_valid:
        print(f"\nWARNING: '{deal['title']}' has a sale_price of 0.00 — verify this is correct")

    return deals

needs_validation(deals)










# the job is to look at normalized deals and valitdate the deals
# what would you need to import first?
# what would the script need to do first?
# prints a warning for every normalized deal that is 0 or orignal price is none, return the list without skipping