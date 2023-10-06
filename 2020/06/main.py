def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(line.rstrip())
    return data


def find_groups(data):
    groups = []
    group = []
    for line in data:
        if line != "":
            group.append(line)
        else:
            groups.append(group)
            group = []

    groups.append(group)

    return groups


def part_one(data):
    groups = find_groups(data)
    group_count = 0
    
    for group in groups:
        found_list = []
        for row in group:
            for letter in row:
                if letter not in found_list:
                    found_list.append(letter)
                    group_count += 1

    return group_count


def part_two(data):
    groups = find_groups(data)
    group_count = 0

    for group in groups:
        found_list = []
        for row in group:
            for letter in row:
                found_list.append(letter)
                if found_list.count(letter) == len(group):
                    group_count += 1
    
    return group_count


if __name__ == "__main__":
    data = read_data("input.txt")

    print(f"The result for part one is {part_one(data)}.")

    print(f"The result for part two is {part_two(data)}.")
