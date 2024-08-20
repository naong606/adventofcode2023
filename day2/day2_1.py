class Game:
    class Round:
        def __init__(self, round_str):
            self.r = 0
            self.g = 0
            self.b = 0

            count_color_strs = round_str.split(", ")
            for count_color_str in count_color_strs:
                count_str, color = count_color_str.split(' ')
                count = int(count_str)

                if color == "red":
                    self.r = count
                elif color == "green":
                    self.g = count
                else: # color == "blue"
                    self.b = count

        def __repr__(self):
            return "Red: {}, Green: {}, Blue: {}".format(self.r, self.g, self.b)

    def __init__(self, game_str):
        self.id = 0
        self.rounds = []

        game_str = game_str[5:]  # Truncate leading 'Game'
        game_id, round_str_concat = game_str.split(": ")
        self.id = int(game_id)

        round_strs = round_str_concat.split("; ")
        for round_str in round_strs:
            self.rounds.append(self.Round(round_str))

def load_games(file_name):
    games = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            games.append(Game(line[:-1] if line[-1] == '\n' else line))
    return games

def is_game_possible(game):
    def get_max_rgb(game):
        maxr, maxg, maxb = 0, 0, 0
        for round in game.rounds:
            maxr = max(maxr, round.r)
            maxg = max(maxg, round.g)
            maxb = max(maxb, round.b)
        return maxr, maxg, maxb

    r, g, b = get_max_rgb(game)
    return r <= 12 and g <= 13 and b <= 14

def get_id(game):
    return game.id

file_name = "input.txt"
games = load_games(file_name)
possible_game_ids = map(get_id, filter(is_game_possible, games))
answer = sum(possible_game_ids)
print(answer)