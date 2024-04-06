def main():
    N = input()
    a = list(map(int, input().split()))

    freq_map = {}
    for num in a:
        freq_map[num] = freq_map.get(num, 0) + 1

    removal_count = 0
    for num, freq in freq_map.items():
        if freq < num:
            removal_count = removal_count + freq
        elif freq > num:
            removal_count = removal_count + (freq - num)

    print(removal_count)

main()
