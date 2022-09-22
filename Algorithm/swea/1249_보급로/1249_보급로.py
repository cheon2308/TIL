# S에서 G까지 가기 위해 도로 복구 작업
# 파여진 깊이에 비례하여 복구 시간 증가
# 복구 시간이 가장 짧은 경로에 대해 복구 시간 구하라
# 깊이 1 == 시간 1

from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(start):
    q = deque()
    # q에 시작위치 넣어주고
    q.append(start)
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        sti, stj = q.popleft()
        for k in range(4):
            dx, dy = sti + di[k], stj + dj[k]
            # 이동가능한 곳이라면
            if 0<=dx<N and 0<=dy<N:
                # 거리 비교하여 최소라면 갱신해주고 큐에 추가.
                if repair[dx][dy] > repair[sti][stj] + road[dx][dy]:
                    repair[dx][dy] = repair[sti][stj] + road[dx][dy]
                    q.append((dx,dy))

    return repair

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 현재 도로 리스트
    road = [list(map(int, list(input()))) for _ in range(N)]
    # 수리하며 지나갈 리스트
    repair = [[100000] * N for _ in range(N)]
    # 시작위치는 0으로 바꿔준다.
    repair[0][0]=0

    bfs((0,0))

    print(f'#{tc} {repair[-1][-1]}')