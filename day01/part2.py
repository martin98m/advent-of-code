
if __name__ == '__main__':
    text_file = open("input.txt", "r")
    # text_file = open("test.txt", "r")
    lines = text_file.read().split('\n')
    lines = list(map(int, lines))

    deeper = 0
    prev = lines[0] + lines[1] + lines[2]
    for idx, x in enumerate(lines[:-2]):
        new = lines[idx] + lines[idx+1] + lines[idx+2]
        if new > prev:
            deeper = deeper + 1
        prev = new

    print(deeper)
