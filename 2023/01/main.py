def read_data(input):
  with open(input) as f:
    data = []
    for line in f:
        data.append(line.rstrip())
  return data


def find_numbers(line):
  numbers = ""
  for digit in line: 
    if digit.isdigit():
      numbers += str(digit)
  return numbers
	
def find_numbers_2(line, dict):
  numbers = ""
  for index, digit in enumerate(line): 
    if digit.isdigit():
      numbers += digit
    else:
      possible_number = line[index:index+5]
      if len(possible_number) > 1 and not possible_number[1].isdigit():
        for key in dict.keys():
          if key in line[index:index+5]:
            numbers += str(dict[key])

  return numbers
	
def first_last_number(number_string): 
  return int(number_string[0] + number_string[-1])
    
def part_one(data):
  number_list = []
  for line in data: 
    number_str = find_numbers(line)
    number = first_last_number(number_str)
    number_list.append(number)
  return sum(number_list)


def part_two(data):
  number_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"} 
  
  number_list = []
  for line in data: 
    number_str = find_numbers_2(line, number_dict)
    number = first_last_number(number_str)
    number_list.append(number)
  return sum(number_list)    


if __name__ == "__main__":
  data = read_data("input.txt")

  print(f"The result for part one is {part_one(data)}.")

  print(f"The result for part two is {part_two(data)}.")
