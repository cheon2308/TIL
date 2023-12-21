[백준 1260_DFS와 BFS](https://www.acmicpc.net/problem/1260)



## 조건
- 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하라
- 이 때, 방문할 수 있는 노드가 여러 개면 숫자가 작은 곳부터 방문
- 정점의 개수, 간선의 개수, 탐색 시작 번호가 주어지고
- M개의 줄에 걸쳐 간선 정보 주어진다.


## 접근 방법
- bfs의 경우 q에 담아줄 때 작은 번호부터 담기 때문에 상관없다.
- 다만 dfs의 경우 큰 번호 먼저 pop되므로 반복문 범위를 뒤에서부터 해준다.


```python
import sys  
input = sys.stdin.readline  
  
# DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력  
# 정점 번호가 작은 것은 먼저 방문한다.  
  
def dfs(V):  
    visited = [0] * (N+1)  
    stack = []  
    stack.append(V)  
  
  
    while stack:  
        sti = stack.pop()  
  
        if visited[sti] == 0:  
            visited[sti] = 1  
            print(sti, end=' ')  
  
        for i in range(len(arr[sti])-1, 0, -1):  
            if arr[sti][i]==1 and visited[i] == 0:  
  
                stack.append(i)  
  
    print()  
  
  
def bfs(v):  
    visited = [0] * (N + 1)  
    q = []  
    q.append(V)  
    visited[V] = 1  
  
    while q:  
        sti = q.pop(0)  
        print(sti, end=' ')  
        for i in range(len(arr[sti])):  
            if arr[sti][i] and visited[i] == 0:  
                q.append(i)  
                visited[i] = 1  
  
  
  
N, M, V = map(int, input().split())  
  
arr = [[0]*(N+1) for _ in range(N+1)]  
  
for i in range(M):  
    a, b = map(int, input().split())  
    arr[a][b] = 1  
  
  
  
dfs(V)  
bfs(V)
```