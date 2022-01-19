#!python
from typing import List, Dict


def readfile_input() -> List:
    return_list = []
    with open("input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        for line in lines:
            stripped_line = line.strip()
            line_list = []
            line_list = list(stripped_line)
            return_list.append(line_list)
    return return_list


def puz_part01():
    input_list = readfile_input()
    gamma_list = []
    epsilon_list = []
    times_change = 0
    line_length = 12
    for entry in input_list:
        if len(entry) > line_length:
            line_length = len(entry)
            times_change += 1
    if times_change != 0:
        print("Need to validate inputs.  Length Changed")
        exit()
    line_pos = 0
    while line_pos < line_length:
        match_dict = {
            "0": 0,
            "1": 0,
        }
        for entry in input_list:
            if entry[line_pos] == "0":
                match_dict["0"] += 1
            elif entry[line_pos] == "1":
                match_dict["1"] += 1
            else:
                print("Character is wrong.  Exiting")
                print(f"{entry[line_pos] =}")
                exit()
        if match_dict["0"] > match_dict["1"]:
            gamma_list.append("0")
            epsilon_list.append("1")
        elif match_dict["1"] > match_dict["0"]:
            gamma_list.append("1")
            epsilon_list.append("0")
        else:
            print("Numbers are not right.  Check them")
            exit()
        line_pos += 1
    num = ""
    gamma_num = int(num.join(gamma_list), 2)
    num = ""
    epsilon_num = int(num.join(epsilon_list), 2)
    print("Part 01")
    print(f"gamma x epsilon = {gamma_num * epsilon_num}")
    print("\n\n")


def find_number(
    sort_list: List,
    sig_number: str,
    line_length: int,
) -> int:
    while True:
        line_pos = 0
        while line_pos < line_length - 1:
            match_dict: Dict = {
                "0": [],
                "1": [],
            }
            for entry in sort_list:
                if entry[line_pos] == "0":
                    match_dict["0"].append(entry)
                elif entry[line_pos] == "1":
                    match_dict["1"].append(entry)
                else:
                    print("Character is wrong.  Exiting")
                    print(f"{entry[line_pos] =}")
                    exit()
            print(f"0s are {len(match_dict['0'])} and 1s are {len(match_dict['1'])}")
            if len(match_dict["0"]) > len(match_dict["1"]):
                if sig_number == "1":
                    sort_list = match_dict["0"]
                elif sig_number == "0":
                    sort_list = match_dict["1"]
            elif len(match_dict["0"]) < len(match_dict["1"]):
                if sig_number == "1":
                    sort_list = match_dict["1"]
                elif sig_number == "0":
                    sort_list = match_dict["0"]
            elif len(match_dict["0"]) == len(match_dict["1"]):
                sort_list = match_dict[str(sig_number)]
            else:
                print("Numbers are not right.  Check them")
                exit()
            line_pos += 1
            print(f"sort_list length is {len(sort_list)}")
            if len(sort_list) == 1:
                break
        if len(sort_list) == 1:
            print(f"length of sort_list = {len(sort_list[0])}")
            break
    print(sort_list)
    num = ""
    return_number = int(num.join(sort_list[0]), 2)
    print(return_number)
    return return_number


def puz_part02():
    input_list = readfile_input()
    times_change = 0
    line_length = 12
    for entry in input_list:
        if len(entry) > line_length:
            line_length = len(entry)
            times_change += 1
    if times_change != 0:
        print("Need to validate inputs.  Length Changed")
        exit()
    oxy_gen_rating = find_number(input_list, "1", line_length=line_length)
    car_gen_rating = find_number(input_list, "0", line_length=line_length)
    print("Part 02")
    print(f"Life Support Rating = {oxy_gen_rating * car_gen_rating}")
    print("\n\n")


def main():
    puz_part01()
    puz_part02()


if __name__ == "__main__":
    main()
