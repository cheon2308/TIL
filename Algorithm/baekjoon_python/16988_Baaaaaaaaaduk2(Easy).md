
[백준 16988 - Baaaaaaaaaduk2 (Easy)](https://www.acmicpc.net/problem/16988)

#### **시간 제한 2초, 메모리 제한 512MB**

## **# 조건**

- 그렇게 모두가 낙담하던 중 누군가가 역사책을 뒤져 인간이 AI에게 승산이 있는 종목을 찾아냈다. 
- 바로 정확히 100년 전에 있었던 이세돌과 알파고의 바둑 대결이었다. 물론 알파고는 그 이후로 발전을 거듭했기에 바둑에서의 승산은 없지만 바둑의 룰을 변형한 Baduk2라는 종목에서는 이세돌이 알파고에게 한 세트를 이긴 것과 같이 인간이 AI에게 승산이 있다고 판단했다.
- Baduk2의 룰은 바둑과 거의 유사하지만 양 선수가 돌을 1개씩 번갈아 두는 것이 아니라 2개씩 둔다는 점이 다르다. 
- 서술의 편의를 위해 상하좌우로 인접한 같은 색 돌의 집합을 그룹이라고 하자. 
- 아래의 판에서는 흑의 그룹과 백의 그룹이 각각 3개씩 존재한다.

![](assets/Pasted%20image%2020230831134942.png)

- Baduk2에서는 일반적인 바둑과 동일하게 자신의 돌로 상대방의 그룹을 빈틈없이 에워싸면 갇힌 돌을 죽일 수 있다. 
- 어느 그룹이 빈틈없이 에워싸였다는 것은 그 그룹 내에 빈 칸과 인접해있는 돌이 하나도 없다는 것과 동치이다.

![](assets/Pasted%20image%2020230831134959.png)

- 그리고 Baduk2에서는 모든 비어있는 칸에 돌을 둘 수 있다. 
- 설령 상대 돌로 둘러싸여 있어 스스로 잡히는 곳이라고 하더라도 상관이 없다. 
- 아래와 같은 상황을 생각해보자.

![](assets/Pasted%20image%2020230831135018.png)

- 두 빨간 칸 모두 백의 입장에서 착수할 경우 연결된 그룹이 흑돌로 둘러싸이게 되어 원래 바둑의 규칙에서는 백의 입장에서 스스로 잡히는 곳이지만 Baduk2에서는 이와 무관하게 백이 빨간 칸 두 곳에 착수해 8개의 흑돌이 들어있는 그룹의 돌을 죽일 수 있다.
- 저항군은 AI에게 Baduk2로 도전장을 내밀었고 AI는 의외로 순순히 도전을 받아들였다. 
- 이제 저항군은 2116년 3월 9일, 인류의 자존심을 건 Baduk2 대결을 시작한다. 
- 그리고 당신에게 인류의 승리를 돕기 위해 현재 판 위에서 돌 2개를 두어 상대 돌을 최대한 많이 죽이게끔 하는 프로그램을 작성하는 임무가 주어졌다. 
- 인류의 명예를 걸고 현재 판이 주어질 때 돌 2개를 두어 죽일 수 있는 상대 돌의 최대 갯수를 구하는 프로그램을 작성하자.

#### **입력**
- 첫째 줄에 바둑판의 행의 갯수와 열의 갯수를 나타내는 N(3 ≤ N ≤ 20)과 M(3 ≤ M ≤ 20)이 한 칸의 빈칸을 사이에 두고 주어진다. 
- 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 
- 각 칸에 들어가는 값은 0, 1, 2이다. 
- 0은 빈 칸, 1은 나의 돌, 2는 상대의 돌을 의미한다. 
- 빈 칸이 2개 이상 존재함과 현재 바둑판에서 양 플레이어 모두 상대방의 돌로 빈틈없이 에워싸인 그룹이 없음이 모두 보장된다.

#### **출력**
- 첫째 줄에 현재 판에서 돌 2개를 두어 죽일 수 있는 상대 돌의 최대 갯수를 출력한다.

## **# 접근 방법**

- BFS를 이용하여 사람이 놓을 수 있는 0의 칸들 중 2개를 뽑는 조합을 순회하며 잡을 수 있는 돌들을 탐색해볼 수 있다.
- 하지만 이 경우 최대 399C2 * N * M번의 연산을 할 수도 있으므로 비효율적이기에 조금 더 효율적인 아이디어를 생각해보았다.
- 흑돌의 무리를 잡기 위해서는 흑돌 주변으로 빈 칸이 최대 2개만 존재하여야 된다.
- 따라서 주어진 바둑판을 순회하며 흑돌을 만난 경우 BFS함수를 돌려준다.
	- BFS를 돌리며 흑돌의 무리를 찾으면서 흑돌의 개수와, 빈 칸의 좌표를 같이 기록해준다.
	- 탐색이 끝난 후 만약 빈 칸의 개수가 2개 이하라면, 빈 칸의 좌표를 저장해둔 temp와 흑돌 그룹의 개수를 return 해준다.
- 빈 칸의 좌표가 존재한다면 black_stone 딕셔너리에 
	- 그룹의 번호  : [(좌표 1),(좌표 2), .. , 흑돌의 개수]로 저장해준다.
- 또한, 나중에 2개씩 조합을 짜기 위하여 빈 칸의 좌표들을 can_leave set에 저장해준다.
- 잡을 수 있는 흑돌의 그룹 탐색이 끝났다면 can_leave 세트에 저장되어 있는 좌표 중 2개씩 조합을 짜서 최대로 잡을 수 있는 흑돌의 개수를 카운트 해준다.
	- 여기서 조심해야 될 점은, 만약 잡을 수 있는 흑돌의 그룹이 1개이거나 놔둘 수 있는 좌표가 1개라면 조합을 짤 수 없으므로
	- black_stone 딕셔너리 value 값의 -1 인덱스 => 흑돌 그룹의 개수를 더해서 바로 출력해주면 된다.
- 이후 can_leave 세트를 combination(can_leave, 2)를 활용하여 조합을 순회한다.
	- 만약 black_stone 그룹의 value의 좌표가 1개라면 
		- 현재 선택한 빈칸 2개중 1개만 있으면 잡을 수 있다.
	- 만약 좌표가 2개라면
		- 2개다 존재해야 잡을 수 있다.
	- 잡을 수 있다면 temp에 값을 더해가면서 현재 조합의 탐색이 끝났다면 result 값을 갱신하면 된다.

```python
import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
from collections import deque, defaultdict  
from itertools import combinations  
  
def bfs(ci, cj):  
    q = deque()  
    q.append((ci, cj))  
    # 주변의 빈 칸의 좌표와 흑돌의 개수 저장  
    temp = set()  
    cnt = 0  
    while q:  
        si, sj = q.popleft()  
        cnt += 1  
        for d in range(4):  
            ni, nj = si+di[d], sj+dj[d]  
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:  
                if arr[ni][nj] == 0:  
                    temp.add((ni, nj))  
                    continue  
                elif arr[ni][nj] == 2:  
                    q.append((ni, nj))  
                    visited[ni][nj] = 1  
    # 빈 칸이 2개 이하여야 잡을 수 있으므로 2개 이하인 경우에만 return으로 넘겨준다.  
    if not len(temp) > 2:  
        return (temp, cnt)  
    else:  
        return (0, 0)  
  
N, M = map(int, input().split())  
arr = [[*map(int, input().split())] for _ in range(N)]  
visited = [[0] * M for _ in range(N)]  
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]  
result = 0  
  
# 흑돌 그룹 탐색하기  
black_stone = defaultdict(list)  
can_leave = set()  
group = 1  
for i in range(N):  
    for j in range(M):  
        if not visited[i][j] and arr[i][j] == 2:  
            visited[i][j] = 1  
            v, c = bfs(i, j)  
            if v:  
                black_stone[group] = list(v)  
                black_stone[group].append(c)  
                for k, u in v:  
                    can_leave.add((k, u))  
                group += 1  
  
# 잡을 수 있는 흑돌의 그룹이 1개이거나 놔둘 수 있는 좌표가 1개라면  
# 2개씩 조합 짤 필요없으므로 바로 카운트 후 출력  
if len(black_stone) == 1 or len(can_leave) == 1:  
    for i, j in black_stone.items():  
        result += j[-1]  
    print(result)  
    exit()  
  
# 놓을 수 있는 곳 조합으로 체크하기  
# 한 군데만 놓아도 잡을 수 있는 흑돌 그룹이라면 => 빈칸 2개중 1개만 존재하면 됨  
# 두 군데 다 놓아야 된다면 => 빈칸 2개다 존재하는지 체크  
for com in combinations(can_leave, 2):  
    temp = 0  
    for b in black_stone:  
        if len(black_stone[b]) == 2:  
            if com[0] in black_stone[b] or com[1] in black_stone[b]:  
                temp += black_stone[b][-1]  
        else:  
            if com[0] in black_stone[b] and com[1] in black_stone[b]:  
                temp += black_stone[b][-1]  
    result = max(result, temp)  
  
print(result)
```

- 항상 느끼지만 바로 효율적인 아이디어를 떠올린다면 좋겠지만 그렇지 못한 경우가 많다.
- 브루트 포스로 아이디어를 생각한 후 시간 또는 메모리를 줄일 수 있는 방법을 고민해보는 것이 항상 많은 도움이 되는 것 같다.