from help_functions import *

if __name__ == "__main__":
    file = open("input.txt").read()
    lines = file.split("\n")

    bingo_numbers, boxes = input_processing(lines)
    board_count = len(boxes)
    boards_won = 0
    for number in bingo_numbers:
        to_remove = []
        for box in boxes:
            check_number_in_box(number, box)
            if check_solved(box):
                boards_won = boards_won + 1
                if boards_won == board_count:
                    box_sum = sum_unmarked(box)
                    print(box_sum*number)
                    exit(0)
                to_remove.append(box)

        for i in to_remove:
            boxes.remove(i)
