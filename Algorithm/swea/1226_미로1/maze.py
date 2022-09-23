import sys
sys.stdin = open("input.txt")

# 미로 16*16
# 가로 x, 세로 y
# 1은 벽, 0은 통로, 2는 출발, 3은 도착

# dfs
def dfs(sti, stj, endi, endj):
    # 스택 생성 및 시작점 넣어주기
    stack = [(sti, stj)]
    # 큐가 비어있지 않다면
    cnt = 0
    while stack:
        sti, stj = stack.pop()
        # 도착했다면 1 리턴
        if sti == endi and stj == endj:
            return cnt
        # 상하좌우 탐색
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni = sti + di
            nj = stj + dj

            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj] != 1:
                stack.append((ni,nj))
                cnt += 1
        # 방문 표시 남겨준다.
        maze[sti][stj] =1

    return 0

# 1. bfs
# def bfs(sti, stj, endi, endj):
#     # 큐 생성 및 시작점 넣어주기
#     q = [(sti, stj)]
#     # 큐가 비어있지 않다면
#     while q:
#         sti, stj = q.pop(0)
#         # 도착했다면 1 리턴
#         if sti == endi and stj == endj:
#             return 1
#         # 상하좌우 탐색
#         for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
#             ni = sti + di
#             nj = stj + dj
#             # 범위를 벗어나지 않고 통로가 있다면
#             if 0<=ni<16 and 0<=nj<16 and maze[ni][nj] != 1:
#                 q.append((ni,nj))
#         # 방문 표시 남겨준다.
#         maze[sti][stj] =1
#
#     return 0
# tc 10개
for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]


    sti, stj, endi, endj = -1, -1, -1, -1
    # 출발, 도착 지점 찾아주기
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                sti, stj = i, j
            if maze[j][i] == 3:
                endi, endj = j, i
        if sti > -1 and stj > -1 and endi > -1 and endj > -1:
            break

    print(f'#{tc} {dfs(sti,stj, endi, endj)}')