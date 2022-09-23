# 5,000개의 버스 정류장
# 노선은 N개, i번째 버스 노선은 번호가 Ai이상, Bi이하인 모든 정류장만 다닌다.
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선 다니는지 구항라

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 버스 노선마다 다니는 정류장
    bus_path = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    # P개의 버스 정류장
    stop_result = [int(input()) for _ in range(P)]

    # 편의를 위해 0번 인덱스
    bus_stop = [0]*5001
    for i, j in bus_path:
        for k in range(i, j+1):
            bus_stop[k] += 1

    print(f'#{tc}', end=' ')
    for l in stop_result:
        print(bus_stop[l], end=' ')
    print()

    # print(bus_stop, stop_result)