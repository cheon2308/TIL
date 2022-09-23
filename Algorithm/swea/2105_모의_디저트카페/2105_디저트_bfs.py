# N x N 모양의 지역에 디저트 카페 모여있다.
# 칸의 숫자는 디저트의 종류
# 카페들 사이에는 대각선 방향 길
# 대각선으로 사각형 모양을 그리며 출발한 카페로 돌아와야한다.

# 같은 종류의 디저트를 먹는 것 싫어한다.
# 한 곳도 안됨, 왔던길도 못돌아감

# 디저트 가장 많이 먹는 경로, 그 때의 디저트 수 출력
# 먹을 수 없는 경우 -1
import sys
from collections import deque
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 초기값 - 먹을수 없는 경우
    result = -1
    # 갈 수 있는 대각선 체크해주고
    # 디저트 종류 리스트에 넣어주기
    # 중간에 한 곳이라도 디저트가 겹친다면 다른 루트 찾아준다.
    cafe = [list(map(int, input().split())) for _ in range(N)]
    dx, dy =[1,1, -1, -1], [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            q = deque()
            # 출발 위치, 디저트의 종류, 회전 카운트, 델타함수 인덱스 = 지나간 방향
            q.append([i, j, [cafe[i][j]], 0, -1])
            while q:
                x, y, dessert, count, ld = q.popleft()
                # 처음 출발위치로 돌아 왔다면 최댓값 갱신
                if x == i and y == j and count == 4:
                    if result < len(dessert):
                        result = len(dessert)

                # 아직 사각형을 그리지 못했다면
                elif count < 5:
                    # 4방향 탐색
                   for d in range(4):
                        if d >= ld:
                            nx, ny = x + dx[d], y + dy[d]

                            # 탐색 가능 지역이라면
                            if 0 <= nx < N and 0 <= ny < N:
                                # 1번 이상 꺾고 도착했다면
                                if nx == i and ny == j and count>1:
                                    # 이전에 지나온 방향이 같다면 -> 꺾지 않았다면 count 그대로
                                    # 아니라면 count +1
                                    if ld == d:
                                        q.append([nx, ny, dessert, count, d])
                                    else:
                                        q.append([nx, ny, dessert, count+1, d])

                                # 중복 디저트 없다면
                                elif cafe[nx][ny] not in dessert:
                                    # 이전에 지나온 방향이 같다면 -> 꺾지 않았다면 count 그대로
                                    # 아니라면 count +1
                                    # 지금 먹으러가는 디저트 + 현재까지 먹은 디저트 종류
                                    if ld == d:
                                        q.append([nx, ny, dessert + [cafe[nx][ny]], count, d])
                                    else:
                                        q.append([nx, ny, dessert + [cafe[nx][ny]], count +1, d])


    print(f'#{tc} {result}')