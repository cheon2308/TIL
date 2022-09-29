import sys
from collections import deque
sys.stdin = open('input.txt')

# N개의 집
# 도로는 단방향 간선이며 이동하는 시간 정해져 있다.
# 1번~N번 번호 붙일 때, 인수의 집 X번
# X번 집으로 오고 가는데 드는 시간 중 가장 오래 걸리는 집의 시간


# ========================================================================================================
### bfs 이용
def bfs(x, visited, path):
    q = deque()
    q.append(x)
    while q:
        start = q.popleft()
        for i in range(len(path[start])):
            if path[start][i]:
                # 도착점 인덱스와 거리
                end, dist = i, path[start][i]
                # 아직 방문하지 않았거나, 도착지에 기록되있는 경로 값이, 현재 가는 경로 값보다 크다면
                # 또한, 최종 목적지가 아니라면
                # and가 or보다 먼저 계산 되므로 괄호 필수!
                if (visited[end] == 0 or visited[end] > visited[start] + dist) and end != x:
                    q.append(end)
                    visited[end] = visited[start] + dist


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    # 오는 경로 -> 출발지에서 도착지로의 경로
    come = [[0]*(N+1) for _ in range(N+1)]
    # 가는 경로 -> 도착지에서 출발지로의 경로
    back = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b,c = map(int, input().split())
        come[a][b] = c
        back[b][a] = c
    # 왔다 갔다 방문기록
    visited_come = [0] * (N + 1)
    visited_back = [0] * (N + 1)
    bfs(X, visited_back, back)
    bfs(X, visited_come, come)
    result = 0
    # 각 집에서 목적지를 왔다갔다 하는 거리 구해주기
    for i in range(N+1):
        a = visited_back[i] + visited_come[i]
        if a >result:
            result = a
    print(come)
    print(back)
    print(f'#{tc} {result}')



###========================================================================================
# heapq 이용
import heapq

T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    result = 0
    path1 = [[] for _ in range(N + 1)]
    path2 = [[] for _ in range(N + 1)]
    goback_cost = [0 for _ in range(N + 1)]  # 왕복 시 각 집에 드는 코스트
    for _ in range(M):
        x, y, c = map(int, input().split())
        path1[x].append((c, y))
        path2[y].append((c, x))

    dist1 = [10 ** 8 for _ in range(N + 1)]
    dist1[X] = 0
    q = path1[X]
    for p1 in path1[X]:
        c, v = p1
        dist1[v] = c

    while q:
        c, v = heapq.heappop(q)
        for c1, w in path1[v]:
            if dist1[w] > c + c1:
                dist1[w] = c + c1
                heapq.heappush(q, (dist1[w], w))

    dist2 = [10 ** 8 for _ in range(N + 1)]
    dist2[X] = 0
    q = path2[X]
    for p2 in path2[X]:
        c, v = p2
        dist2[v] = c

    while q:
        c, v = heapq.heappop(q)
        for c1, w in path2[v]:
            if dist2[w] > c + c1:
                dist2[w] = c + c1
                heapq.heappush(q, (dist2[w], w))

    # print(dist1)
    # print(dist2)
    # print()
    for i in range(1, len(dist1)):
        if result < dist1[i] + dist2[i]:
            result = dist1[i] + dist2[i]

    print(f'#{tc} {result}')