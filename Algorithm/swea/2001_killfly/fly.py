import sys
sys.stdin = open('input.txt')

def sum_fly(s, e):
    kill = 0
    max_fly = 0
    i,j =0
    while i != N-1 and j != N-1:
    for i in range(M):
        for j in range(M):
            kill += fly[i][j]



T = int(input())

for tc in (1, T+1):
    # N은 5이상 15이하, M은 2이상 N이하, 각 영역 파리 갯수 30이하
    # MxM 크기의 파리채를 내리쳐 최대한 많은 파리
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]


    print(max_fly)
