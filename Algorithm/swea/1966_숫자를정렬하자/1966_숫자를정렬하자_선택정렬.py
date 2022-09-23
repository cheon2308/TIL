import sys
sys.stdin = open('input.txt')

# N을 오름차순으로 정렬하라

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    num = list(map(int, input().split()))
    idx = 0
    for i in range(N-1):
        idx = i
        for j in range(i+1, N):
            if num[idx] > num[j]:
                idx = j

        num[i], num[idx] = num[idx],num[i]


    print(f'#{tc}',  *num)