import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    d = [0, 1, 2, 4]
    n = int(input())
    while len(d) != n+1 :
        d.append(sum(d[-3:]))
    print(d[-1])