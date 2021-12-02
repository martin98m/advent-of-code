
if __name__ == '__main__':
    lines = open("input.txt").readlines()
    my_tuples = []
    for line in lines:
        val = line.split()
        my_tuples.append((val[0], int(val[1])))

    x = y = aim = 0
    for command, value in my_tuples:
        if command == "forward":
            x = x + value
            y = y + aim * value
        elif command == "up":
            aim = aim - value
        elif command == "down":
            aim = aim + value
    print(x * y)