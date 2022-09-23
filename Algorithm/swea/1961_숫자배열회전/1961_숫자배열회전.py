# N x N 행렬이 주어질 때
# 90도 270도 360도로 회전한 모양 출력
# 90도 270도 360도는 회전한 모양 사이에만 공백이 존재함

## 첫번째방법

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(input().split()) for _ in range(N)]

    arr90, arr180, arr270 = [],[],[]
    # 90도로 회전 -> 열의 마지막 행부터 거꾸로 읽는 것과 같다.
    # 123   741    987
    # 456 - 852 -  654
    # 789   963    321

    # rotate 변수에 한 행의 문자열을 만들어주고
    # 각 회전 리스트에 추가해준다.
    for i in range(N):
        rotate = ''
        for j in range(N-1, -1,-1):
            rotate += arr[j][i]
        arr90.append(rotate)

    for i in range(N):
        rotate = ''
        for j in range(N - 1, -1, -1):
            rotate += arr90[j][i]
        arr180.append(rotate)

    for i in range(N):
        rotate = ''
        for j in range(N - 1, -1, -1):
            rotate += arr180[j][i]
        arr270.append(rotate)

    print(f'#{tc}')
    for i in range(N):
        print(arr90[i], end=' ')
        print(arr180[i], end=' ')
        print(arr270[i], end=' ')
        print()

### 2번째 방법

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
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
            for j in range(len(arr) - 1, -1, -1):
                num += str(arr[j][i])
            result.append(num)

        for k in range(N):
            arr[k] = result[len(result) - N + k]

        cnt += 1

    print(f'#{tc}')
    cnt = 0

    for i in range(N):
        print(result[i], result[i + N], result[i + 2 * N])
