def remove_strings(array, index, value):
    new_arr = []
    for item in array:
        if item[index] != value:
            new_arr.append(item)
    return new_arr


def count_zero_one(array, index):
    zero = one = 0
    for x in array:
        if x[index] == "0":
            zero = zero + 1
        else:
            one = one + 1
    return zero, one


def array_looping(array, compare, if_true, if_else):
    len_a = len(array[0])

    for index in range(0, len_a):
        zero, one = count_zero_one(array, index)
        if compare(zero, one):
            array = remove_strings(array, index, if_true)
        else:
            array = remove_strings(array, index, if_else)
        if len(array) == 1:
            return array


def compare_co(zero, one):
    return True if one >= zero else False


def compare_ox(zero, one):
    return True if one >= zero else False


if __name__ == '__main__':
    file_lines = open("input.txt", "r").read().splitlines()

    final_ox = array_looping(file_lines, compare_ox, "0", "1")
    final_co2 = array_looping(file_lines, compare_co, "1", "0")

    final_ox = int(str(final_ox[0]), 2)
    final_co2 = int(str(final_co2[0]), 2)
    print(final_ox * final_co2)
