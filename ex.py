import sys
from collections import deque
input = sys.stdin.readline

# 가지고 있는 정점의 수 기록해줄 함수
def subtree(root):
    # 본인 포함이므로 1로 시작한다.
    count[root] =1
    for i in tree:
        for j in i:


# 정점 수 N, 루트번호 R, 쿼리의 수 Q
N, R, Q = map(int, input().split())

# 간선 입력해줄 리스트
tree = [[] for _ in range(N+1)]
count = [0] *(N+1)
for i in range(N-1):
    # 무방향 이므로 a[b]와 b[a] 둘 다 넣어준다.
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
print(tree)
subtree(R)

# 정점 u

for j in range(Q):
    u = int(input())
    print(count[u])
