
if __name__ == '__main__':
    lines = open("input.txt").readlines()
    my_tuples = []
    for line in lines:
        val = line.split()
        my_tuples.append((val[0], int(val[1])))

    x = y = 0
    for command, value in my_tuples:
        if command == "forward":
            x = x + value
        elif command == "up":
            y = y - value
        elif command == "down":
            y = y + value
    print(x*y)
