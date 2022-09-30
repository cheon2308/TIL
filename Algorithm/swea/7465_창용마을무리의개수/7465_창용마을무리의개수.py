import sys
sys.stdin = open('input.txt')

# =========================================================
# 1 ~ N명의 사람
# 서로 알고 있는 관계일 수도 있고, 아닐 수 있다.
# 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면, 이러한 사람들을 모두 다 묶어서 하나의 무리
# =========================================================

def dfs(person):

    result = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            # 조 +1
            result +=1
            visited[i] = 1
            stack = [i]

        while stack:
            idx = stack.pop()
            for i in range(1, N+1):
                # 투표용지에 썻고 아직 조에 속하지 않았다면
                if person[idx][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    stack.append(i)

    return result


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    person = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        person[a][b] = 1
        person[b][a] = 1

    visited = [0] * (N+1)


    print(f'#{tc} {dfs(person)}')




# =======================================================================
# 서로소 집합 알고리즘으로 해결
def find(x):
    while x != tree[x]:
        x = tree[x]
    return x


def union(a, b):
    a, b = find(a), find(b)
    tree[a] = b


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    tree = list(range(V + 1))

    for a, b in edges:
        union(a, b)

    # 정답 구하기
    answer = set()
    for i in range(1, V + 1):
        answer.add(find(i))

    print(f'#{tc} {len(answer)}')