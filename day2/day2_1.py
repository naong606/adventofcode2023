def load_games(file_name):
    # TODO
    pass

def is_game_possible(game):
    def get_max_rgb(game):
        # TODO
        pass

    r, g, b = get_max_rgb(game)
    return r <= 12 and g <= 13 and b <= 14

def get_id(game):
    # TODO
    pass

file_name = "input.txt"
games = load_games(file_name)
answer = map(get_id, filter(is_game_possible, games))
print(answer)