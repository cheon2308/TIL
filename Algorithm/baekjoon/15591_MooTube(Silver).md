
[백준 15591_MooTube(Silver)](https://www.acmicpc.net/problem/15591)


#### 시간 제한 2초, 메모리 제한 512MB

## 조건

- 농부 존은 MooTube라는 동영상 공유 서비스를 만들었다.
- MooTube 에서 농부 존의 소들은 재밌는 동영상들을 서로 공유할 수 있다.
- 소들은 MooTube에서 1부터 N까지 번호가 붙여진 (1<=N<=5000) 개의 동영상을 올려놓았는데 어떻게하면 그들이 좋아할 만한 새 동영상을 찾을 수 있을지 괜찮은 방법을 떠올리지 못함
- 농부 존은 모든 MooTube 동영상에 대해 “연관 동영상” 리스트를 만들기로 했다. 
	- 이렇게 하면 소들은 지금 보고 있는 동영상과 연관성이 높은 동영상을 추천 받을 수 있을 것이다.
- 존은 두 동영상이 서로 얼마나 가까운 지를 측정하는 단위인 “USADO”를 만들었다. 
- 존은 N-1개의 동영상 쌍을 골라서 직접 두 쌍의 USADO를 계산했다. 
	- 그 다음에 존은 이 동영상들을 네트워크 구조로 바꿔서, 각 동영상을 정점으로 나타내기로 했다. 
	- 또 존은 동영상들의 연결 구조를 서로 연결되어 있는 N-1개의 동영상 쌍으로 나타내었다. 
	- 좀 더 쉽게 말해서, 존은 N-1개의 동영상 쌍을 골라서 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재하도록 했다. 
	- 존은 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO 중 최솟값으로 하기로 했다.
- 존은 어떤 주어진 MooTube 동영상에 대해, 값 K를 정해서 그 동영상과 USADO가 K 이상인 모든 동영상이 추천되도록 할 것이다. 
- 하지만 존은 너무 많은 동영상이 추천되면 소들이 일하는 것이 방해될까 봐 걱정하고 있다! 
- 그래서 그는 K를 적절한 값으로 결정하려고 한다. 
	- 농부 존은 어떤 K 값에 대한 추천 동영상의 개수를 묻는 질문 여러 개에 당신이 대답해주기를 바란다.



#### 입력

- 입력의 첫 번째 줄에는 N과 Q가 주어진다. (1 ≤ Q ≤ 5,000)
- 다음 N-1개의 줄에는 농부 존이 직접 잰 두 동영상 쌍의 USADO가 한 줄에 하나씩 주어진다. 
- 각 줄은 세 정수 pi, qi, ri (1 ≤ pi, qi ≤ N, 1 ≤ ri ≤ 1,000,000,000)를 포함하는데, 이는 동영상 pi와 qi가 USADO ri로 서로 연결되어 있음을 뜻한다.
- 다음 Q개의 줄에는 농부 존의 Q개의 질문이 주어진다. 
	- 각 줄은 두 정수 ki와 vi(1 ≤ ki ≤ 1,000,000,000, 1 ≤ vi ≤ N)을 포함하는데, 이는 존의 i번째 질문이 만약 K = ki라면 동영상 vi를 보고 있는 소들에게 몇 개의 동영상이 추천될 지 묻는 것이라는 것을 뜻한다.


#### 출력

- Q개의 줄을 출력한다.
- i번째 줄에는 농부 존의 i번째 질문에 대한 답변이 출력되어야 한다.



## 접근 방법

- 우선 정점간의 가중치를 기록할 node 리스트를 생성해준다.
- 입력받는 USADO 를 출발노드에 (도착노드, usado) 로 기록해준다.
- 또한, 각 정점별로 다른 정점에 가는 최소값을 기록하기 위한 weight 이차원 행렬을 만들어준다.
- 주어지는 질문 수만큼 돌며 bfs를 진행해준다.
- bfs 함수에서 방문한 적 없고, k보다 크다면 q에 넣어준다.


```python

import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
from collections import deque  
  
def bfs(usado, start):  
    q = deque()  
    q.append(start)  
    visited = [0] *(N+1)  
    result = 0  
    while q:  
        curNode = q.popleft()  
        for nextNode, value in node[curNode]:  
            if visited[nextNode] == 0 and nextNode != start:  
                if value >= usado:  
                    result += 1  
                    q.append(nextNode)  
                    visited[nextNode] = 1  
    return result  
  
N, Q = map(int, input().split())  
  
node = [[] for _ in range(N+1)]  
for _ in range(N-1):  
    a, b, c = map(int, input().split())  
    node[a].append((b, c))  
    node[b].append((a, c))  
  
  
for _ in range(Q):  
    k, v = map(int, input().split())  
  
    print(bfs(k,v))
```



### 다른 분 코드
- MST를 Kruskal 알고리즘을 이용해 풀어주었다.
- 시간효율적으로 많은 차이가 발생.. 
- 더 열심히 풀어봐야 될듯

```python

"""  
존은 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO 중 최솟값으로 하기로 했다.  
"""  
import sys,copy  
input=sys.stdin.readline  
from collections import deque  
  
def Find(x): # 유니온 파인드의 Find 함수  
    if x!=disjoint[x]:  
        disjoint[x] = Find(disjoint[x])  
    return disjoint[x]  
  
def Union(a,b): # 유니온 파인드의 Union 함수  
    a=Find(a) ; b=Find(b)  
  
    if a==b:  
        return  
    if a>b:  
        disjoint[a]=b  
        dp[b]+=dp[a]  
    else:  
        disjoint[b]=a  
        dp[a]+=dp[b]  
  
N,Q=map(int,input().split())  
  
graph=[] # 트리를 저장할 그래프를 선언한다.  
dp=[1]*(N+1)  
  
for i in range(N-1):  
    a,b,c=map(int,input().split())  
    graph.append((a,b,c))  
  
graph.sort(key=lambda x:-x[2])  
graph=deque(graph)  
L=[ list(map(int,input().split())) for _ in range(Q) ] # 쿼리를 입력받는다.  
Query=copy.deepcopy(L) # 쿼리를 미리 복사한다.  
  
L.sort(key=lambda x:-x[0]) # k 값이 높은 순서대로 정렬한다.  
disjoint=[ i for i in range(N+1) ] # 분리집합을 위한 배열을 만든다.  
  
D={} # 오프라인 쿼리를 위한 딕셔너리  
for K,V in L: # 쿼리 실행.  
    while graph and graph[0][2]>=K:  
        if Find(graph[0][0])!=Find(graph[0][1]):  
            Union(graph[0][0] , graph[0][1])  
            graph.popleft()  
    D[(K,V)] = dp[Find(V)]-1  
  
for K,V in Query: # 이전의 복사해둔 쿼리를 사용한다.  
    print(D[(K,V)]) # 그때의 딕셔너리 값을 출력한다.
```