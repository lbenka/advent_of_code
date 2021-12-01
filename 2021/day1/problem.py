def ver_1():
    counter = -1
    current_num = 0

    with open("./2021/day1/in1.txt") as file:

        for line in file.readlines():
            num = int(line)

            if num > current_num:
                counter += 1
            current_num = num

    print(counter)


# ----
def ver_2():
    counter = -1
    current_num = 0

    size_of_sliding_window = 3

    measurements = []
    with open("./2021/day1/in1.txt") as file:

        for line in file.readlines():
            measurements.append(int(line))

    for index, _ in enumerate(measurements):
        num = sum(measurements[index : index + size_of_sliding_window])

        if num > current_num:
            counter += 1
        current_num = num

    print(counter)


ver_2()
