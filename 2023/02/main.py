def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(line.rstrip().split(": ")[1])
    return data



def part_one(data):
    condition = {"red": 12, "green": 13, "blue": 14}
    game_result = []
    
    for game_nr, row in enumerate(data): 
        games = row.split(";")
        
        game_result.append(1)
        
        for game_set in games:
            game_set = game_set.split(", ")
            for color in game_set: 
                [val, col] = color.split()
    
                if int(val) > condition[col]:
                    game_result[game_nr] = 0

    game_sum = 0
    for nr, game in enumerate(game_result):
        if game == 1:
            game_sum += nr+1

    return game_sum


def part_two(data):
    game_result = []
    
    for game_nr, row in enumerate(data): 
        low = {"red": 0, "green": 0, "blue": 0}
        games = row.split(";")
        
        # game_result.append(1)
        
        for game_set in games:
            game_set = game_set.split(", ")
            for color in game_set: 
                [val, col] = color.split()
                low[col] = max(int(val), low[col])
        
        game_result.append(low["red"] * low["green"] * low["blue"])
        print(f'Game: {game_nr+1}, lowest: {low}, product: {low["red"] * low["green"] * low["blue"]}')
        print(game_result)
    return sum(game_result)


if __name__ == "__main__":
    data = read_data("input.txt")

    print(f"The result for part one is {part_one(data)}.")

    print(f"The result for part two is {part_two(data)}.")
