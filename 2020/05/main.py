def read_data(input):
    with open(input) as f:
        data = []
        for line in f:
            data.append(line.rstrip())

    return data


def convert_to_binary(text):
    binary = ""
    for i in text:
        if i == "F" or i == "L":
            binary = binary + "0"
        elif i == "B" or i == "R":
            binary = binary + "1"
    return binary


def find_row(text):
    binary = convert_to_binary(text[:-3])
    row = int(binary, 2)

    return row


def find_column(text):
    binary = convert_to_binary(text[-3:])
    column = int(binary, 2)

    return column


def part_one(data):
    highest_id = 0

    for boarding_pass in data:
        row = find_row(boarding_pass)
        column = find_column(boarding_pass)
        seat_id = row * 8 + column

        if seat_id > highest_id:
            highest_id = seat_id

    return highest_id


def part_two(data):
    seat_ids = []

    for boarding_pass in data:
        row = find_row(boarding_pass)
        column = find_column(boarding_pass)
        seat_id = row * 8 + column

        seat_ids.append(seat_id)

    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids:
            return i

    return "There is no free seat"


if __name__ == "__main__":
    data = read_data("input.txt")

    print(f"The result for part one is {part_one(data)}.")

    print(f"The result for part two is {part_two(data)}.")
