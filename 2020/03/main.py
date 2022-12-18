def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(line.rstrip())
    return data

def recalculate_pos(x, x_max):
    if x < x_max:
        return x
    else: 
        return x % x_max

def is_tree(point):
    if point == "#":
        return True
    elif point == ".":
        return False
    else:
        print(f"Somethings wrong, point is {point}")

def move_point(data, slope):
    n_trees = 0
    x, y = 0, 0

    slope_x, slope_y = slope

    while y <= len(data)-slope_y-1:
        x += slope_x
        y += slope_y

        point = data[y][recalculate_pos(x,len(data[0]))]
        
        if is_tree(point):
            n_trees += 1

    return n_trees

def part_one(data):
    return move_point(data, [3,1])

def part_two(data): 
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    trees_mult = 1

    for slope in slopes: 
        trees_mult *= move_point(data,slope)

    return trees_mult


if __name__ == "__main__":
    data = read_data('input.txt')

    print(f'The result for part one is {part_one(data)}.')

    print(f'The result for part two is {part_two(data)}.')

