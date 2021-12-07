def fish_produced(fish_days, days_remaining):
    # print("X", fish_days, days_remaining)
    fish_sum = 1
    x = days_remaining - fish_days
    if x <= 0:
        return fish_sum
    else:
        for i in range(x, 0, -7):
            # print(i)
            fish_sum = fish_sum + new_fish(i)
        return fish_sum


    # (3,1) => 1
    # (3,2) => 1
    # (3,3) => 1
    # (3,4) => 1 + 1(0)
    # (3,5) => 1 + 1(1)
    # (3,6) => 1 + 1(2)
    # (3,7) => 1 + 1(3)
    # (3,8) => 1 + 1(4)
    # (3,9) => 1 + 1(5)
    # (3,10) => 1 + 1(6)
    # (3,11) => 1 + 1(7)+1(0)
    # (3,12) => 1 + 1(8)+1(1)
    # (3,13) => 1 + 1(9)[1(1)]+1(2)
    # (3,14) => 1 + 1(10)[1(2)]+1(3)


def new_fish(days_remaining):
    new_fish_count = 1
    # no new fish
    if days_remaining < 10:
        return new_fish_count
    else:
        for i in range(days_remaining-9, 0, -7):
            # print("f",i)
            new_fish_count = new_fish_count + new_fish(i)
        return new_fish_count


if __name__ == '__main__':
    # text_file = open("input.txt", "r")
    text_file = open("test.txt", "r")
    lines = [int(x) for x in text_file.read().split(",")]
    # lines = [6]
    # print(fish_produced(lines[0], 10))
    total_sum = 0
    # print(total_sum)
    days_max = 42
    for fish in lines:
        total_sum = total_sum + fish_produced(fish, days_max)
        # print(fish_produced(fish, 1))
    print("Y=", total_sum)

    # for i in range(10, -1, -1):
    #     print(i)