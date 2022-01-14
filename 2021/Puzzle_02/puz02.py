#!python

from typing import List


def read_file() -> List:
    return_list = []
    with open("input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        for line in lines:
            split_list = line.split()
            return_list.append([split_list[0], int(split_list[1])])
    return return_list


def puz_part01():
    input_list = read_file()
    forward_location = 0
    depth_location = 0
    for movement_list in input_list:
        if movement_list[0] == "forward":
            forward_location += movement_list[1]
        elif movement_list[0] == "up":
            depth_location -= movement_list[1]
        elif movement_list[0] == "down":
            depth_location += movement_list[1]
        else:
            print(movement_list[0])
            exit()
    print("Part 01")
    print(f"Forward Movement = {forward_location} ")
    print(f"Depth = {depth_location} ")
    print(f"forward x depth = {forward_location * depth_location}")
    print("\n\n")


def puz_part02():
    input_list = read_file()
    forward_location = 0
    depth_location = 0
    aim_location = 0
    for movement_list in input_list:
        if movement_list[0] == "forward":
            forward_location += movement_list[1]
            if aim_location != 0:
                depth_location = depth_location + (aim_location * movement_list[1])
            elif aim_location == 0:
                depth_location = depth_location
        elif movement_list[0] == "up":
            aim_location -= movement_list[1]
        elif movement_list[0] == "down":
            aim_location += movement_list[1]
        else:
            print(movement_list[0])
            exit()
    print("Part 02")
    print(f"Forward Movement = {forward_location} ")
    print(f"Depth = {depth_location} ")
    print(f"Aim = {aim_location} ")
    print(f"forward x depth = {forward_location * depth_location}")
    print("\n\n")


def main():
    puz_part01()
    puz_part02()


if __name__ == "__main__":
    main()
