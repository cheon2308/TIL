# 5650. 핀볼게임

# NxN 크기의 핀볼 게임판에 정사각형 블록과 4가지 형태의 삼각형 블록
# 추가적 웜홀과 블랙홀
# 1 왼아래 2 왼위 3 오위 4 오아래 5 정사각
# 웜홀 - 육각형,  블랙홀 꽃모양
# ==========================================================================
# 작은 핀볼 하나가 상, 하, 좌, 우 중 한 뱡향 무브
# 블록이나 웜홀 또는 블랙홀 안만난다면 현재 방향 유지
# 수평이나 수직면 만날 경우 방향 바꿔 돌아오고
# 경사면 만나면 직각으로 꺾인다.
# 벽은 만나도 돌아온다.
# ==========================================================================
# 웜홀에 빠지면 동일한 숫자의 반대편 웜홀로 돌아오며 진행방향은 그대로 유지
# (웜홀은 반드시 쌍으로 주어지며, 입력에서는 6이상 10이하의 숫자로 표시)
# 블랙홀 만나면 종료
# 출발 위치로 돌아와도 종료
# 점수는 벽이나 블록에 부딪히는 횟수
# ==========================================================================
# 게임판위에서 출발 위치와 진행 방향 임의 선정 가능할 때,
# 게임에서 얻을 수 있는 점수의 최댓값 구하라
# ==========================================================================




def game(sx, sy, sd):
    global pinball, hole
    score = 0
    tx, ty, nd = sx, sy, sd

    while True:
        tx, ty = tx + di[nd], ty + dj[nd]

        # 범위 내에 존재한다면
        if 0<=tx<N and 0<=ty<N:
            # 그 때 블록을 만났을 경우
            if pinball[tx][ty] in range(1,6):
                block_type = pinball[tx][ty]
                # 점수 증가
                score +=1
                nd = move[block_type][nd]
                continue

            # 웜홀은 만난 경우
            elif pinball[tx][ty] in range(6,11):
                hole_type = pinball[tx][ty]
                if (tx, ty) == hole[hole_type][0]:
                    tx, ty = hole[hole_type][1]
                else:
                    tx, ty = hole[hole_type][0]

                continue

            # 만약 블랙홀은 만난 경우
            elif pinball[tx][ty] == -1:
                return score

            # 시작점일 경우
            elif (tx, ty) == (sx, sy):
                return score
            # 만약 그냥 빈 칸인 경우
            else:
                continue
        # 벽을 만났을 경우
        else:
            nd = (nd +2) % 4
            score +=1


import sys
sys.stdin = open('input.txt')

# 웜홀은 6-10
# 블랙홀은 -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pinball = [[*map(int, input().split())] for _ in range(N)]


    # 상하좌우
    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 진행방향
    # 좌 - 1,상   2,하
    # 우 - 3,하   4,상
    # 하 - 1,우   4,좌
    # 상 - 2,우   3,좌

    # 핀 볼의 진행방향에 따라 벽을 만났을 때 변화
    # 첫 인덱스 = 벽의 번호
    # 작은 인덱스 = 상하좌우
    move = [[],
             [2, 3, 1, 0],
             [1, 3, 0, 2],
             [3, 2, 0, 1],
             [2, 0, 3, 1],
             [2, 3, 0, 1]]

    # 웜홀 위치
    hole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if 6 <= pinball[i][j] <= 10:
                hole[pinball[i][j]].append((i,j))



    # 출발 위치와 진행 방향을 임의로 선정가능
    # 따라서 2중 반복문 안에서 방향에 따른 dfs
    max_result = 0
    for i in range(N):
        for j in range(N):
            if pinball[i][j] == 0:
                for k in range(4):
                    score = game(i, j, k)
                    max_result = max(score, max_result)

    print(f'#{tc} {max_result}')




























