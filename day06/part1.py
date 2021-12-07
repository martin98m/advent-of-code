def decrese_count(array):
    new_count = 0
    for id,idk in enumerate(array):
        # print(array[id])
        if array[id] == 0:
            array[id] = 6
            new_count = new_count + 1
        else:
            array[id] = array[id] - 1
    for i in range(0, new_count):
        array.append(8)
    return array


if __name__ == '__main__':
    # text_file = open("input.txt", "r")
    text_file = open("test.txt", "r")
    # lines = [int(x) for x in text_file.read().split(",")]
    lines = [6]
    # for line in lines:
    #     print(line)

    for day in range(0, 15):
        # print("Day:" + str(day+1))
        lines = decrese_count(lines)
        # print(lines)

    print(len(lines))