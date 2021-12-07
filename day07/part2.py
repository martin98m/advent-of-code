def fuel_cost(len):
    cost = 0
    for i in range(1,len+1):
        cost = cost + i
    return cost

def avg(arr):
    sum = 0
    for x in arr:
        sum = sum + x
    print(sum / len(arr))
    return sum // len(arr)

if __name__ == '__main__':
    text_file = open("input.txt", "r")
    # text_file = open("test.txt", "r")
    lines = [int(x) for x in text_file.read().split(",")]
    res = []
    max_pos = lines[0]
    for i in lines:
        if i > max_pos:
            max_pos = i
    for i in range(avg(lines) -5, avg(lines) + 5):
        fuel = 0
        for x in lines:
            fuel = fuel + fuel_cost(abs(x - i))
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
    # print("-------------")
    # print(fuel_cost(0))
    # print(fuel_cost(1))
    # print(fuel_cost(2))
    # print(fuel_cost(3))
    # print(fuel_cost(4))
    # print(fuel_cost(5))