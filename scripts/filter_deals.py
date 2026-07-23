#import read_games as rg
#games = rg.sample


def calc_discount(orig, sale):
    discount = ((orig - sale)/orig) * 100
    return discount


def filter_discount(discount_percent, source):
    filtered = [game for game in source if (calc_discount(game['original_price'], game['sale_price']) >= discount_percent)]
    return filtered
            


#example = filter_discount(50, games)
#rg.display_games(example)
