#!python

from typing import List


def read_file() -> List[int]:
    return_list = []
    with open("input.txt", "r", encoding="utf-8") as input_file:
        number_line = int(input_file.readline())
        return_list.append(number_line)
    print(return_list)
    return return_list


def main():
    read_file()


if __name__ == "__main__":
    main()
