import sys
sys.stdin = open('input.txt')

#====================================================
# N명의 직원
# N개의 해야할 일
# i번 직원이 j번 일을 하면 성공할 확률 Pij
# 주어진 일이 모두 성공할 확률의 최댓값
#====================================================


# 행 번호, 확률 곱
def check(a,cnt):
    global result
    if cnt <= result:
        return

    if a == N:
        result = cnt
        return

    for i in range(N):
        if not visited[i]:
            # 방문하지 않은 곳이라면 방문기록남겨주고
            visited[i] = 1
            # 다음 행 재귀 + 누적 확률 곱
            check(a + 1, cnt * percent[a][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            percent[i][j] = percent[i][j] / 100

    result = 0
    # 각 열마다 방문기록 표시해주면 된다.
    visited = [0] * N
    check(0,1)
    print(f'#{tc} {result * 100:6f}')