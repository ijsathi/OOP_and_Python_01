def Max_Split(s):
    count = 0
    balanced_str = []
    balance = 0
    current_str = ""

    for char in s:
        current_str = current_str + char
        if char == 'L':
            balance = balance + 1
        else:
            balance = balance - 1

        if balance == 0:
            count = count + 1
            balanced_str.append(current_str)
            current_str = ""

    return count, balanced_str

s = input()

count, balanced_str = Max_Split(s)

print(count)
for string in balanced_str:
    print(string)
