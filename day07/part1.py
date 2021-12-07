if __name__ == '__main__':
    text_file = open("input.txt", "r")
    # text_file = open("test.txt", "r")
    lines = [int(x) for x in text_file.read().split(",")]
    res = []
    max_pos = lines[0]
    for i in lines:
        if i > max_pos:
            max_pos = i
    for i in range(0, max_pos):
        fuel = 0
        for x in lines:
            fuel = fuel + abs(x - i)
        res.append(fuel)
    min = res[0]
    id = 0
    i = 0
    for x in res:
        if x < min :
            id = i
            min = x
        i = i + 1
    print(min)
    print(id)
    print(res)