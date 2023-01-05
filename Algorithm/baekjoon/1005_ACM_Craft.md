
[백준 1005_ACM Craft](https://www.acmicpc.net/problem/1005)


## 접근

- 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다.
- 매 게임시작 시 건물을 짓는 순서가 주어진다.
- 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.
 
![[Algorithm/baekjoon/assets/Pasted image 20230105092026.png]]

- 이번 게임에서는 다음과 같이 건설 순서 규칙이 주어졌다. 
	- 1번 건물의 건설이 완료된다면 2번과 3번의 건설을 시작할수 있다. (동시에 진행이 가능하다) 
	- 그리고 4번 건물을 짓기 위해서는 2번과 3번 건물이 모두 건설 완료되어야지만 4번건물의 건설을 시작할수 있다.
	- 따라서 4번건물의 건설을 완료하기 위해서는 우선 처음 1번 건물을 건설하는데 10초가 소요된다.
	- 그리고 2번 건물과 3번 건물을 동시에 건설하기 시작하면 2번은 1초뒤에 건설이 완료되지만 아직 3번 건물이 완료되지 않았으므로 4번 건물을 건설할 수 없다. 
	- 3번 건물이 완성되고 나면 그때 4번 건물을 지을수 있으므로 4번 건물이 완성되기까지는 총 120초가 소요된다.

- 프로게이머 최백준은 애인과의 데이트 비용을 마련하기 위해 서강대학교배 ACM크래프트 대회에 참가했다! 
- 최백준은 화려한 컨트롤 실력을 가지고 있기 때문에 모든 경기에서 특정 건물만 짓는다면 무조건 게임에서 이길 수 있다. 
- 그러나 매 게임마다 특정건물을 짓기 위한 순서가 달라지므로 최백준은 좌절하고 있었다.
- 백준이를 위해 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.



#### 입력

- 첫째 줄에는 테스트케이스의 개수 T가 주어진다. 
- 각 테스트 케이스는 다음과 같이 주어진다. 첫째 줄에 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다) 
- 둘째 줄에는 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다. 
- 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다) 
- 마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.



## 접근 방법

- 선행 되어야 하는 작업이 있으므로 위상정렬을 이용해준다.
- 차수를 기록해주고, 0번 차수인 건물들을 q에 담아주는데 dp를 이용하여 누적 시간을 기록해준다.
- while문을 돌려주며 위상 정렬을 적용해준다. 
- 0번 차수 건물들에 기록된 건물들의 차수를 -1씩 해주며 dp의 값에 누적해준다.


```python
import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
from collections import deque  
  
  
def dp(q, finish):  
    while q:  
        now_loc = q.popleft()  
        for i in build[now_loc]:  
            degree[i] -= 1  
            dp[i] = max(dp[i], dp[now_loc] + D[i])  
  
            if degree[i] == 0:  
                q.append(i)  
  
        if degree[finish] == 0:  
            print(dp[finish])  
            break  
  
  
T = int(input())  
for tc in range(T):  
    N, K = map(int, input().split())  
  
    D = [0] + [*map(int, input().split())]  
    degree = [0] * (N+1)  
    build = [[] for _ in range(N+1)]  
  
    for _ in range(K):  
        a, b = map(int, input().split())  
        build[a].append(b)  
        degree[b] += 1  
  
    q = deque()  
    dp = [0] * (N+1)  
    for i in range(1,N+1):  
        if degree[i] == 0:  
            q.append(i)  
            dp[i] = D[i]  
    dest = int(input())  
    bfs(q, dest)
```