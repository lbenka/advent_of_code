from os import path
from pathlib import Path

init_file_path = Path(__file__).parent / "in.txt"


def load_file(file_path):
    with open(file_path) as file:
        return file.readlines()


DOWN_STRING = "down"
UP_STRING = "up"
FORWARD_STRING = "forward"


# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.


def get_num(line: str) -> int:
    return int(line.split()[1])


def ver_1():
    forward_counter = 0
    depth_counter = 0

    lines = load_file(init_file_path)

    for line in lines:
        if FORWARD_STRING in line:
            forward_counter += get_num(line)
        if DOWN_STRING in line:
            depth_counter += get_num(line)

        if UP_STRING in line:
            depth_counter -= get_num(line)

    return forward_counter * depth_counter


# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#   It increases your horizontal position by X units.
#   It increases your depth by your aim multiplied by X.


def ver_2():
    aim = 0
    forward_counter = 0
    depth_counter = 0

    lines = load_file(init_file_path)

    for line in lines:
        num = get_num(line)
        if FORWARD_STRING in line:
            forward_counter += num

            depth_counter += (aim * num)

        if DOWN_STRING in line:
            aim += num

        if UP_STRING in line:
            aim -= num

    return forward_counter * depth_counter


if __name__ == "__main__":
    # val = ver_1()
    # 1507611

    val = ver_2()
    # 1880593125
    print(val)
