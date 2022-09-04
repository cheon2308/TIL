import sys
sys.stdin = open("input.txt")

# NxN 크기의 미로, 출발지 - 목적지
# 최소 몇 칸의 지나면 도착하는지 알아내는 프로그램
# 있는 경우 최소 칸 수, 없는 경우 0

def BFS(sti, stj, endi, endj): # 현재좌표 입력
    # 방문 리스트
    visited = [[-1] * N for _ in range(N)]

    # 큐 생성 및 시작지점 추가, 시작지점 방문표시
    q = [(sti, stj)]
    # 최단 경로에 출발, 도착지점은 포함하지 않으므로 0으로 해준다.
    visited[sti][stj] = 0

    # 스택이 비어있지 않다면
    while q:
        # 출발 정점 변경
        # 행, 열 순서로 넣어줫으니 순서 그대로
        sti, stj = q.pop(0)
        # 상하좌우 탐색
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
        #     범위를 벗어나지 않고                        벽이 아니고 탐색 가능하다면
            if 0<=sti+di<N and 0<=stj+dj<N and maze[sti+di][stj+dj]!=1 and visited[sti+di][stj+dj]==-1:
                # q에 추가해주고 방문기록 남긴다.
                q.append((sti+di,stj+dj))
                # 방문할 정점 목록에 도착지점이 있다면 현재 정점까지의 경로 출력
                if (endi, endj) in q:
                    return visited[sti][stj]
                # 직전 경로 +1 을 해준다.
                visited[sti+di][stj+dj] = visited[sti][stj] + 1

    # 경로 없다면 0
    return 0
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj, endi, endj = -1, -1, -1, -1
    # 출발 지점, 도착 지점 찾아준다.
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] ==3:
                endi, endj = i, j
            # 출발지점은 밑에서부터 찾아준다.
            if maze[N-1-i][N-1-j] == 2:
                sti, stj = N-1-i, N-1-j

        if sti > -1 and stj > -1 and endi > -1 and endj > -1:
            break

    print(f'#{tc} {BFS(sti, stj, endi, endj)}')