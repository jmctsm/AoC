#!python


def readfile_input():
    boards_return = []
    call_list_return = []
    with open("input.txt", "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        line_list = []
        for line in lines:
            if line == "\n":
                continue
            stripped_line = line.strip()
            if "," in stripped_line:
                call_list_return = stripped_line.split(",")
            elif " " in stripped_line:
                line_list.append(stripped_line.split())
            if len(line_list) == 5:
                boards_return.append(line_list)
                line_list = []
    return (call_list_return, boards_return)


def count_board():
    pass


def check_bingo(game_boards):
    for game_board in range(len(game_boards)):
        for game_line in range(len(game_boards[game_board])):
            if game_boards[game_board][game_line] == ["X", "X", "X", "X", "X"]:
                print("Bingo_Found")


def puz_part01():
    call_list, input_list = readfile_input()
    value_found = False
    for call_number in call_list:
        for game_board in range(len(input_list)):
            for game_line in range(len(input_list[game_board])):
                for game_number in range(len(input_list[game_board][game_line])):
                    if call_number == input_list[game_board][game_line][game_number]:
                        input_list[game_board][game_line][game_number] = "X"
                        value_found = check_bingo(input_list)
                        if value_found:
                            print(
                                f"Value to put in website = {call_number * value_found}"
                            )

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
