import sys
sys.stdin = open('input.txt')


#  A도시 출발하여 B도시로 가는 길이 존재하는지 조사

# 최대 2개의 갈림길, 일방 통행
# A와 B는 숫자 0과 99로 고정
# 모든 길은 순서쌍으로 나타나다.
# 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재

def dfs(N):
    visited[N] = 1
    # 전체 정점을 조사한다.
    for i in range(1, len(line)):
        # 방문할 곳에 길이 있고, 아직 방문전이라면
        if line[N][i] == 1 and visited[i] == 0:
            dfs(i)

for tc in range(1, 11):
    N, total = map(int,input().split())
    # 경로 리스트 받기
    course = list(map(int, input().split()))
    # 전체 정점 리스트
    line = [[0]*100 for _ in range(100)]
    # 간선 기록해주기
    # 경로리스트의 짝수 인덱스 출발, 홀수 인덱스 도착
    # 2개씩 뛰어넘으며 [j-1][j]로 기록해준다.

    for j in range(1, len(course), 2):
        line[course[j-1]][course[j]] = 1


    # 방문한 곳을 확인할 배열
    visited = [0] * 100
    # A도시에서 출발
    dfs(0)
    # B도시를 방문했는지 출력
    print(f'#{tc} {visited[99]}')


















# # 교수님 풀이
# def dfs(n):
#     # 출발지 0을 방문 표시
#     visited[n] = 1
#
#     # 0에서 출발하므로 1부터 조사
#     for w in range(1, 101):
#         # n(출발지)에서 w(다음 행성지)로 이동 가능여부 파악
#         # 0 2 -> G[0][2]에 True 표시 해 두었음
#         # 이전에 방문한 적 없는 곳만 방문
#             # 어느쪽에서 왔든 99에 도착만하면 되므로
#             # 한명이라도 방문한 적 있다면 상관 X
#         if G[n][w] == 1 and visited[w] == 0:
#             # n에서 w로 이동하였으므로 w 부터 다시 조사
#             dfs(w)
#
# # tc 10개
# for _ in range(10):
#     # tc 번호, 간선의 개수
#     tc, E = map(int, input().split())
#     # 이동 가능 정보
#     data = list(map(int, input().split()))
#
#     # 방문 표시 할 리스트 (정점 최대 100개)
#     visited = [0] * 101
#
#     # 인접 행렬
#     G = [[0 for _ in range(101)] for _ in range(101)]
#
#     # 넘겨받은 이동 가능 정보는 순서쌍으로 이루어 져있음
#     # 2개가 한 세트로, 0 2는 0번에서 2번으로 이동 가능의 의미
#     # 방향성 그래프 이므로, 한쪽 방향으로만 체크
#     for i in range(0, len(data), 2):
#         G[data[i]][data[i+1]] = 1
#
#     dfs(0)
#
#     print(f'#{tc} {visited[99]}')