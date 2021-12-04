from help_functions import *

if __name__ == "__main__":
    file = open("input.txt").read()
    lines = file.split("\n")

    bingo_numbers, boxes = input_processing(lines)

    for number in bingo_numbers:
        for box in boxes:
            check_number_in_box(number, box)
            if check_solved(box):
                box_sum = sum_unmarked(box)
                print(box_sum*number)
                exit(0)
