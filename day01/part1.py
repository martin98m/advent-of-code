
if __name__ == '__main__':
    text_file = open("input.txt", "r")
    # text_file = open("test.txt", "r")
    lines = text_file.read().split('\n')
    lines = list(map(int, lines))

    deeper = 0
    prev = lines[0]
    for x in lines:
        if x > prev:
            deeper = deeper + 1
        prev = x

    print(deeper)
