def maximum_operations(N, A):
    operations = 0
    
    while all(num % 2 == 0 for num in A):
        A = [num // 2 for num in A]
        operations = operations + 1
    return operations

# Input
N = input()
A = list(map(int, input().split()))

# Output
print(maximum_operations(N, A))
