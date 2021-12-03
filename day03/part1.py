if __name__ == '__main__':
    file_lines = open("input.txt", "r").read().splitlines()
    arr_len = len(file_lines[0])
    total_sum = [0] * arr_len
    gamma = [0] * arr_len
    epsilon = [0] * arr_len

    for line in file_lines:
        for i in range(0, arr_len):
            total_sum[i] = total_sum[i] + int(line[i])

    for i in range(0, arr_len):
        gamma[i] = 1 if total_sum[i] > 500 else 0
        epsilon[i] = 0 if total_sum[i] > 500 else 1

    gamma_str = ''.join(str(e) for e in gamma)
    epsilon_str = ''.join(str(e) for e in epsilon)

    print(int(gamma_str, 2) * int(epsilon_str, 2))
