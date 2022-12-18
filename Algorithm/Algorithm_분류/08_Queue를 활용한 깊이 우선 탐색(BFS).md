
그래프를 탐색하는 방법에는 크게 두 가지가 있다.

-   **깊이 우선 탐색(Depth First Search, DFS)**  
    -   저번에 봤듯이 Stack 또는 재귀의 단계를 활용하여 구현
-   **너비 우선 탐색(Breadth First Search, BFS)**
    -   탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후, 방문헀던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
    -   인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로 **선입선출 형태의 자료구조인 큐를 활용**

> **순서**

![](https://k.kakaocdn.net/dn/d1RkhS/btrKqEegceM/irzjiPZs25YkDaAE9LYKNK/img.png)

```PYTHON
def BFS(G, v): # 그래프 G, 탐색 시작점 v
    visited = [0]*(n+1)		# n: 정점의 개수
    queue = [] 			# 큐 생성
    queue.append(v) 	# 시작점 v를 큐에 삽입
    while queue:		# 큐가 비어있지 않은 경우
    	t = queue.pop(0) 	#  큐의 첫번째 원소 반환
        if not visited[t]:	# 방문되지 않은 곳이라면
            visited[t] = True 	# 방문한 것으로 표시
            visit(t)
            for i in G[T]:		# t와 연결된 모든 정점에 대해
            	if not visited[i]: 		# 방문되지 않은 곳이라면
                	queue.append(i) 	# 큐에 넣기
```

> **구현 예제**

1. 초기 상태

-   Visited 배열 초기화
-   Q 생성
-   시작점 enqueue

![](https://k.kakaocdn.net/dn/zGgpi/btrKsPslmED/K9e6dcETs8bBZgGDFvh5u0/img.png)

![](https://k.kakaocdn.net/dn/cCE9xY/btrKqGiQHv2/cRBdjfp5m6YDXqQYQEkLYK/img.png)

2. A점부터 시작

-   dequeue: A
-   A 방문 표시
-   A 인접점 enqueue

![](https://k.kakaocdn.net/dn/AxxcW/btrKtAPsUUd/QsPVFC9lQLn7vpNjOdNkl1/img.png)

![](https://k.kakaocdn.net/dn/bNdUa9/btrKlTpZQv3/r1MiTlqKefLd4OmPAy8Hek/img.png)

3. 탐색 진행

-   dequeue: B
-   B 방문한 것으로 표시
-   B의 인접점 enqueue

![](https://k.kakaocdn.net/dn/Hx8CC/btrKpP8tH2Y/PgryXWJegwPHk2ARiATAlK/img.png)

![](https://k.kakaocdn.net/dn/R3XUP/btrKsFcoHyL/gfGYmJUBMUE1IHEk2lGFpK/img.png)

4. 탐색진행

-   3번을 계속 반복한다.

![](https://k.kakaocdn.net/dn/bIK04s/btrKq53IsqN/Zq8fGuqPcU5UnxPJS0Lmq1/img.png)

![](https://k.kakaocdn.net/dn/Lvdn3/btrKqGb3hGv/QkHUpPPNN9rmeRzNOLmqK0/img.png)

5. Q가 빈다면 탐색종료

![](https://k.kakaocdn.net/dn/bgA8wx/btrKp6vkSgU/hhTk7z2EiKS15mSUGibBBK/img.png)

![](https://k.kakaocdn.net/dn/u2n6d/btrKtAopjGJ/7iYJAxnIoOL4szHoD6gcL0/img.png)

이렇게 BFS의 과정에 대해서 살펴봤다.