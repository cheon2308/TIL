import sys
sys.stdin = open('input.txt')
# 노즐은 +형태라 + 또는 x로만 분사
# M의 세기에 따라 M칸 파리
# N의 크기, 세기는 칸을 벗어나도 상관없다.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 파리 리스트 받아주고
    fly = [list(map(int, input().split())) for _ in range(N)]
    # + 최다킬
    # x 최다킬
    max_kill = 0
    max_kill_plus =0
    max_kill_x = 0
    # 전체 리스트 돌며
    for i in range(len(fly)):
        for j in range(len(fly)):
            # 한번 뿌렸을 때의 킬 기록
            kill = 0
            # 좌표 안에 존재한다면
            # 중심 더해주고
            kill += fly[i][j]
            # + 스프레이 범위 더해준다.

            for k in range(1, M):
                # 세로부터
                # 상
                if 0 <= i-k < N:
                    kill += fly[i-k][j]
                # 하
                if 0 <= i+k <N:
                    kill += fly[i+k][j]

                # 가로
                # 좌측
                if 0 <= j-k < N:
                    kill += fly[i][j-k]
                # 우측
                if 0 <= j+k<N:
                    kill += fly[i][j+k]

            if kill>max_kill:
                max_kill = kill
                #print(max_kill, i, j)
    # x 범위
    for i in range(len(fly)):
        for j in range(len(fly)):
            # 한번 뿌렸을 때의 킬 기록
            kill = 0
            # 좌표 안에 존재한다면
            # 중심 더해주고
            kill += fly[i][j]
            # + 스프레이 범위 더해준다.

            for k in range(1, M):
                # 좌측 위

                if 0 <= i - k < N and 0<=j-k<N:
                    kill += fly[i - k][j-k]
                # 좌측 아래
                if 0 <= i + k < N and 0 <= j - k < N:
                    kill += fly[i + k][j - k]
                # 우측 위
                if 0 <= i - k < N and 0 <= j + k < N:
                    kill += fly[i - k][j + k]
                # 우측
                if 0 <= i + k < N and 0 <= j + k < N:
                    kill += fly[i + k][j + k]

            if kill > max_kill:
                max_kill = kill




    print(f'#{tc} {max_kill}')

