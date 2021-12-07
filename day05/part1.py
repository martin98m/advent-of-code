def count_val(val, field):
    count = 0
    for x in field:
        for y in x:
           if y > val:
            count = count + 1
    return count


def max_val(field):
    val = 0
    for x in field:
        for y in x:
           if y > val:
            val = y
    return val


def print_field(field):
    for x in field:
        print(x)
    print("\n")


def increase_val(start, end, array):
    x1, y1, x2, y2 = start[0], start[1], end[0], end[1]
    print(x1, y1, x2, y2)
    if x1 != x2 and y1 != y2:
        return array
    print("fine")


    if x1 == x2:
        if y1 > y2:
            for i in range(y2, y1+1):
                array[i][x1] = array[i][x1] + 1
        else:
            for i in range(y1, y2+1):
                array[i][x1] = array[i][x1] + 1
    if y1 == y2:
        if x1 > x2:
            for i in range(x2, x1+1):
                array[y1][i] = array[y1][i] + 1
        else:
            # print(x1, x2+1)
            for i in range(x1, x2+1):
                array[y1][i] = array[y1][i] + 1
    return array


if __name__ == '__main__':
    text_file = open("input.txt", "r")
    # text_file = open("test.txt", "r")
    lines = text_file.readlines()
    formated_input = []
    for line in lines:
        line = line.replace(" -> ", ",").replace("\n", "")
        line = line.split(",")
        print(line)
        left = (int(line[0]), int(line[1]))
        right = (int(line[2]), int(line[3]))
        formated_input.append((left, right))

    max_x = max_y = 0
    for x in formated_input:
        max_x = x[0][0] if x[0][0] > max_x else max_x
        max_x = x[1][0] if x[1][0] > max_x else max_x
        max_y = x[0][1] if x[0][1] > max_y else max_y
        max_y = x[1][1] if x[1][1] > max_y else max_y
    print(max_x, max_y)
    # max_x = 9
    # max_y = 9
    # field = [[0]*max_x]*max_y
    field = []
    b = []
    for j in range(0, max_x+1):
        b.append(0)
    for i in range(0, max_y+1):
        field.append(b.copy())
    # print_field(field)
    # ass = [9,5]
    # bas = [3,5]
    # print_field(field)
    # increase_val([0,9], [5,9], field)
    # print_field(field)
    # increase_val([0,9], [2,9], field)
    # print_field(field)
    arr = field.copy()
    for start, end in formated_input:
        print(start, end)
        arr = increase_val(start, end, arr)

    # print_field(arr)
    max_v = max_val(arr)
    print(max_v)
    count_v = count_val(1, arr)
    print(count_v)
