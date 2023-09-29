def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(line.rstrip().split())

    return data


def read_passport(lst):
    passportlist = []
    _dict = {}
    for line in lst:
        if line == []:
            passportlist.append(_dict)
            _dict = {}

        else:
            for i in line:
                key, value = i.split(":")
                _dict[key] = value

    passportlist.append(_dict)

    return passportlist


def test_validity(passport):
    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False

    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False

    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False

    if passport["hgt"].endswith("cm"):
        if int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193:
            return False
    elif passport["hgt"].endswith("in"):
        if int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
            return False
    else:
        return False

    if passport["hcl"][0] != "#":
        return False
    else:
        if len(passport["hcl"]) != 7:
            return False
        else:
            for char in passport["hcl"][1:]:
                if char not in [
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                ]:
                    return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if len(passport["pid"]) != 9:
        return False
    else:
        if not passport["pid"].isdigit():
            return False

    return True


def part_one(data):
    passports = read_passport(data)
    count = 0
    for passport in passports:
        if (len(passport) == 7 and "cid" not in passport) or len(passport) == 8:
            count += 1
    return count


def part_two(data):
    passport_list = read_passport(data)
    count = 0

    for passport in passport_list:
        if (len(passport) == 7 and "cid" not in passport) or len(passport) == 8:
            if test_validity(passport):
                count += 1
    return count


if __name__ == "__main__":
    data = read_data("input.txt")

    print(f"The result for part one is {part_one(data)}.")

    print(f"The result for part two is {part_two(data)}.")
