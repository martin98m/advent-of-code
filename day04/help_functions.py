def input_processing(input_array):
    numbers = [int(i) for i in input_array[0].split(',')]
    bingo_boxes = []
    bingo_box = []
    for idx in range(2, len(input_array)):
        if input_array[idx] == "":
            bingo_boxes.append(bingo_box)
            bingo_box = []
            continue
        bingo_box.append([(int(i), False) for i in input_array[idx].split()])
    return numbers, bingo_boxes


def check_row_or_col(row):
    for val, checked in row:
        if not checked:
            return False
    return True


def check_solved(bingo_box):
    bingo = False
    # check rows
    for row in bingo_box:
        if check_row_or_col(row):
            return True
    # check cols
    for i in range(0, len(bingo_box[0])):
        col = [row[i] for row in bingo_box]
        if check_row_or_col(col):
            return True
    return bingo


def check_number_in_box(value, box):
    for row in range(0, len(box)):
        for col in range(0, len(box[row])):
            val, mark = box[row][col]
            if val == value:
                box[row][col] = (val, True)


def sum_unmarked(bingo_box):
    final_sum = 0
    for row in range(0, len(bingo_box)):
        for col in range(0, len(bingo_box[row])):
            val, mark = bingo_box[row][col]
            if mark is False:
                final_sum = final_sum + val
    return final_sum


def print_box(box):
    for row in box:
        print(row)
