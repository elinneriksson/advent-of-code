def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(line.rstrip())
    return data


def allow_password(data,type):
    password_allowed = 0
    for val in data:
        limits, nr, password = val.split()
        limit_min, limit_max = [int(i) for i in limits.split('-')]
        nr = nr.split(':')[0]
        
        if type == 'range':
            char_count = password.count(nr)
            
            if char_count in range(limit_min,limit_max+1):
                password_allowed += 1

        elif type == 'index':
            if nr in password[limit_min-1] and nr in password[limit_max-1]:
                continue
            elif nr in password[limit_min-1] or nr in password[limit_max-1]:
                password_allowed += 1

    return password_allowed


def part_1(data):
    return allow_password(data, 'range')

def part_2(data):
    return allow_password(data, 'index')


if __name__ == "__main__":
    data = read_data('input.txt')

    print(f'The result for part one is {part_1(data)}.')

    print(f'The result for part two is {part_2(data)}.')