
if __name__ == '__main__':
    lines = open("input.txt").readlines()
    my_tuples = []
    for line in lines:
        val = line.split()
        my_tuples.append((val[0], int(val[1])))

    x = 0
    y = 0
    for command in my_tuples:
        if command[0] == "forward":
            x = x + command[1]
        elif command[0] == "up":
            y = y - command[1]
        elif command[0] == "down":
            y = y + command[1]
    print(x*y)
