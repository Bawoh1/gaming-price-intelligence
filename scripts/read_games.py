import json


def read_games(filepath):
    with open(filepath, 'r') as file:
        games = json.load(file)
    return games


def display_games(games):
    for game in games:
        print(f"\nTitle: {game['title']}, Original Price: {game['original_price']}, Sale Price: {game['sale_price']}, Store: {game['store']}")



sample = read_games('data/raw/sample_games.json')
#display_games(sample)
