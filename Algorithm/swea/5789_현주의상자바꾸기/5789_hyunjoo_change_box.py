# 1-N번까지의 N개의 상자
# Q회 동안 일정 범위의 연속 상자를 동일 수자로 변경
# i 번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # 작업할 박스
    box = [list(map(int, input().split())) for _ in range(Q)]

    # 현재 박스
    # 편하게 하기위해서 0번 인덱스 추가
    boxes = [0] * (N+1)
    cnt = 0
    # cnt로 작업 횟수 늘려주기
    for i, j in box:
        cnt +=1
        for k in range(i, j+1):
            boxes[k] = cnt

    print(f'#{tc}', *boxes[1:])
