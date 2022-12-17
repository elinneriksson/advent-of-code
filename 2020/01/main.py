
def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(int(line.rstrip()))
    return data

def find_2020(data,num):
    for i, value_1 in enumerate(data):
        for j in range(i+1, len(data)):
            value_2 = data[j]

            if num == 2:
                
                if (value_1 + value_2) == 2020:
                    return value_1*value_2
            
            elif num == 3:
                for k in range(j+1, len(data)):
                    value_3 = data[k]

                    if (value_1 + value_2 + value_3) == 2020:
                        return value_1*value_2*value_3

def part_1(data):
    return find_2020(data,2)

def part_2(data):
    return find_2020(data,3)


if __name__ == "__main__":
    data = read_data('input.txt')

    print(f'The result for part one is {part_1(data)}.')

    print(f'The result for part two is {part_2(data)}.')