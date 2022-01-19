#!python

from pprint import PrettyPrinter


def readfile_input():
    boards_return = []
    call_list_return = []
    game_board = []
    with open("input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        line_list = []
        line_counter = 0
        for line in lines:
            if line == "\n":
                print(f"{len(line_list) = }")
                if len(line_list[0]) > 5:
                    call_list_return = line_list[0]
                    line_list = []
                    line_counter = 0
                    continue
                elif len(line_list) == 5:
                    game_board.append(line_list)
                    print(game_board)
                    line_counter += 1
                    if line_counter == 4:
                        boards_return.append(game_board)
                        line_counter = 0
                        game_board = []
                    line_list = []
                    continue
                else:
                    print("line_list is not the right number")
                    print(f"{line_list = }")
                    exit()
            else:
                stripped_line = line.strip()
                if "," in stripped_line:
                    line_list.append(stripped_line.split(","))
                else:
                    line_list.append(stripped_line.split())
    return (call_list_return, boards_return)


def puz_part01():
    call_list, input_list = readfile_input()
    print(f"{call_list = }")
    counter = 0
    print(input_list)
    for game_board in input_list:
        for game_line in game_board:
            print(f"Game {counter}")
            print(game_line)
            counter += 1
        print("\n\n")
    print("Part 01")
    print("\n\n")


def puz_part02():
    print("Part 02")
    print("\n\n")


def main():
    puz_part01()
    puz_part02()


if __name__ == "__main__":
    main()
