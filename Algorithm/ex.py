import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N=int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = ''
    for i in range(len(arr)):
        num = ''
        for j in range(len(arr)):
            num += str(arr[i][j])
        arr[i] = num

    result = []
    cnt = 0
    while cnt != 3:
        for i in range(len(arr)):
            num = ''
            for j in range(len(arr)-1,-1,-1):
                num += str(arr[j][i])
            result.append(num)

        for k in range(N):
            arr[k] = result[len(result)-N+k]

        cnt +=1

    print(f'#{tc}')
    cnt = 0

    for i in range(N):
        print(result[i], result[i+N], result[i+2*N])
