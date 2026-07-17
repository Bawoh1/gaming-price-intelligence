import json
import read_games as rg
games = rg.sample


def calc_discount(orig, sale):
    discount = ((orig - sale)/orig) * 100
    return discount


def filter_discount(discount_percent):
    filtered = [game for game in games if (calc_discount(game['original_price'], game['sale_price']) >= discount_percent)]
    return filtered
            


example = filter_discount(50)
print(example)
#rg.display_games(example)
