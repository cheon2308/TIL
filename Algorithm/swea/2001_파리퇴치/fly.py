import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N은 5이상 15이하, M은 2이상 N이하, 각 영역 파리 갯수 30이하
    # MxM 크기의 파리채를 내리쳐 최대한 많은 파리
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    idx = M-1


    # 행 열 N- M+1까지 반복
    # 내려칠 곳 탐색
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            # 파리채 크기만큼 돌면서
            # 해당 좌표에서 파리채로 잡을 수 있는 파리수 더해준다.
            for x in range(i, i+M):
                for y in range(j, j+M):
                    kill += fly[x][y]

            if kill > max_kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')