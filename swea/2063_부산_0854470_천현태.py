N = int(input())

A = list(map(int, input().split()))

A.sort()

middle = N // 2

print(A[middle])
