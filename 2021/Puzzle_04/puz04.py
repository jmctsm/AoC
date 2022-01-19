#!python


def readfile_input():
    boards_return = []
    call_list_return = []
    game_board = []
    with open("input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        line_list = []
        line_counter = 0
        for line in lines:
            stripped_line = line.strip()
            if stripped_line == "":
                if len(line_list) > 5:
                    call_list_return = line_list
                    line_list = []
                    continue
                elif len(line_list) == 5:
                    game_board.append(line_list)
                    if line_counter == 4:
                        boards_return.append(game_board)
                        line_counter = 0
                        game_board = []
                        line_list = []
                    else:
                        line_counter += 1
                    continue
                else:
                    print("line_list is not the right number")
                    print(f"{line_list = }")
                    exit()
            elif "," in stripped_line:
                line_list = stripped_line.split(",")
            else:
                line_list = stripped_line.split()
    return (call_list_return, boards_return)


def puz_part01():
    call_list, input_list = readfile_input()
    print(call_list)
    for game_board in input_list:
        for game_line in game_board:
            print(game_line)
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
