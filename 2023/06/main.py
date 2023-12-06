def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(line.rstrip().split(": ")[1])
    return data



def part_one(data):
    time = data[0].split()
    distance = data[1].split()
    wins = 1
    for race, t in enumerate(time):
        t = int(t)
        limit = int(distance[race])
        
        nr_wins = 0
        
        for x in range(0,t+1):
            if -x*x + t*x > limit:
                nr_wins += 1
                # print(f'{x} gives time over {limit}')
        wins *= nr_wins
        
    return wins


def part_two(data):
    time = data[0].replace(" ","")
    distance = data[1].replace(" ","")

    t = int(time)
    limit = int(distance)
    
    nr_wins = 0
    
    for x in range(14,t-13):
        if -x*x + t*x > limit:
            nr_wins += 1

        
    return nr_wins


if __name__ == "__main__":
    data = read_data("input.txt")

    print(f"The result for part one is {part_one(data)}.")

    print(f"The result for part two is {part_two(data)}.")