import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def count_val(val, field):
    zero = one = count = 0

    for x in field:
        for y in x:
            if y > val:
                count = count + 1
            elif y == 0:
                zero = zero + 1
            elif y == 1:
                one = one + 1
    return zero, one, count


def print_field(field):
    for x in field:
        print(x)
    print("\n")


def increase_val(start, end, array):
    x1, y1, x2, y2 = start[0], start[1], end[0], end[1]
    # print(x1, y1, x2, y2)
    # print((abs(x1-x2) == abs(y1-y2)))
    valid = False
    if x1 == x2 or y1 == y2:
        valid = True
    if abs(x1 - x2) == abs(y1 - y2):
        valid = True
    # if x1 != x2 and y1 != y2 and (abs(x1-x2) != abs(y1-y2)):
    #     return array
    if not valid:
        print("not valid")
        return array
    # print("fine")
    if x1 == x2:
        if y1 > y2:
            for i in range(y2, y1+1):
                array[i][x1] = array[i][x1] + 1
        else:
            for i in range(y1, y2+1):
                array[i][x1] = array[i][x1] + 1
    elif y1 == y2:
        if x1 > x2:
            for i in range(x2, x1+1):
                array[y1][i] = array[y1][i] + 1
        else:
            for i in range(x1, x2+1):
                array[y1][i] = array[y1][i] + 1
    else:
        # print("else")
        a = x2 if x1 > x2 else x1
        b = x1 if x1 > x2 else x2
        # c = y2 if y1 > y2 else y2
        # d = y1 if y1 > y2 else y2
        i = 0
        # print(start, end)
        for x in range(a, b+1):
            # print(x)
            if y1 > y2 and x1 < x2:
                # print(x, y1 - i)
                array[y1-i][x] = array[y1-i][x] + 1
                i = i + 1
            elif y1 > y2 and x1 > x2:
                # print(x, y2 + i)
                array[y2 + i][x] = array[y2 + i][x] + 1
                i = i + 1
            elif x1 > x2 and y1 < y2:
                # print(x, y2 - i)
                array[y2-i][x] = array[y2-i][x] + 1
                i = i + 1
            elif x1 < x2 and y1 < y2:
                array[x][x] = array[x][x] + 1
            else:
                # for y in range(y1, y2+1,):
                print("BAAAAAAAAAAAD")
                # array[x][x] = array[x][x] + 1
    return array


if __name__ == '__main__':
    text_file = open("input.txt", "r")
    # text_file = open("test.txt", "r")
    lines = text_file.readlines()
    formated_input = []
    for line in lines:
        line = line.replace(" -> ", ",").replace("\n", "")
        line = line.split(",")
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
    # increase_val([1,1], [3,3], field)
    # print_field(field)
    # increase_val([0,9], [2,9], field)
    # print_field(field)
    arr = field.copy()
    # print(len(formated_input))
    id = 0
    nam = ""
    for start, end in formated_input:
        # print(start, end)
        arr = increase_val(start, end, arr)
        # xas = np.array(arr)
        # sns.set()
        # import matplotlib.pyplot as plt
        #
        # plt.figure(figsize=(10, 10))
        # ax = sns.heatmap(xas, cbar=None, xticklabels=False, yticklabels=False)
        # nam = "00"+str(id) if id < 10 else "0"+str(id) if id < 100 else str(id)
        # name = nam + "-" + str(start) + str(end)
        # id = id + 1
        # print(name)
        # plt.savefig(str(name), bbox_inches='tight', dpi=1000)

        # print_field(arr)

    # print_field(arr)
    # max_v = max_val(arr)
    # print(max_v)
    count_v = count_val(1, arr)
    print(count_v)

    # xas = np.array(arr)
    # sns.set()
    # import matplotlib.pyplot as plt
    #
    # plt.figure(figsize=(10, 10))
    # ax = sns.heatmap(xas, cbar=None, xticklabels=False, yticklabels=False)
    #
    # plt.savefig("vents.png", bbox_inches='tight', dpi=1000)


    # plt.imshow(xas, interpolation='none')
    # plt.show()
