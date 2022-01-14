#!python

from typing import List


def read_file() -> List[int]:
    return_list = []
    with open(f"input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        for line in lines:
            return_list.append(int(line.strip()))
    return return_list


def part_one():
    input_list = read_file()
    count = 0
    inc_count = 0
    dec_count = 0
    same_count = 0
    for number in input_list[1:]:
        if number > input_list[count]:
            inc_count += 1
        elif number < input_list[count]:
            dec_count += 1
        elif number == input_list[count]:
            same_count += 1
        count += 1
    print("PART 1")
    print(f"{inc_count = }")
    print(f"{dec_count = }")
    print(f"{same_count = }")
    print("\n\n")


def part_two():
    input_list = read_file()
    start_ind = 0
    end_ind = 2
    new_list_numbers = []
    while end_ind <= len(input_list):
        try:
            num_sum = (
                input_list[start_ind] + input_list[start_ind + 1] + input_list[end_ind]
            )
        except IndexError as e:
            print("List is done")
        new_list_numbers.append(num_sum)
        start_ind += 1
        end_ind += 1
    count = 0
    inc_count = 0
    dec_count = 0
    same_count = 0
    for number in new_list_numbers[1:]:
        if number > new_list_numbers[count]:
            inc_count += 1
        elif number < new_list_numbers[count]:
            dec_count += 1
        elif number == new_list_numbers[count]:
            same_count += 1
        count += 1
    print("PART 2")
    print(f"{inc_count = }")
    print(f"{dec_count = }")
    print(f"{same_count = }")
    print("\n\n")


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
