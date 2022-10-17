
[프로그래머스 순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191](https://school.programmers.co.kr/learn/courses/30/lessons/49191)



## 조건

- n명의 권투선수가 참여했고 각각 1번부터 n번까지 번호
- A 선수가 B 선수보다 실력이 좋다면 항상 이긴다.
- 하지만 몇몇 경기 결과를 분실하여 정확한 순위 매기기 힘들다.
- 선수의 수 n, 결과를 담은 2차원 배열 reuslt가 주어질 때,
- 정확하게 순위를 매길 수 있는 선수의 수를 return



## 접근 방법

- 정확한 순위를 매길 수 있다는 것 -> 모든 선수와 경기를 하였다는 뜻이다.
- 따라서, 그래프 연결 고리를 만들어 주고 사이클이 있는 번호의 수만 출력해준다.
- visited 함수에 기록을 해준 후 각 선수의 방문 기록에 1을 카운트하였을 때 n-1이 되어주어야 한다.


위와 같이 했을 때는 모든 선수와 경기를 한 선수만 알 수 있다.

- 예제와 같은 경우처럼 2번 선수가 4등인 경우 5번 선수가 4등에게 졌기 때문에 자동으로 5등이 되는 것 같이 더 많은 연결 관계가 필요
- 따라서, 그래프 연결 관계를 만들어 줄 때, 내가 이긴 선수가 이긴 선수는 나도 이기는 것을 기록해준다.
- 반대로 내가 진 선수가 진 선수는 나도 진다.
- 등수를 알 필요는 없기 때문에 위와 마찬가지로 기록된 경기 수가 n-1이라면 cnt +1


```python

# 그래프 연결 관계를 만들어 줄 때, 내가 이긴 선수가 이긴 선수는 나도 이기는 것을 기록해준다.  # 반대로 내가 진 선수가 진 선수는 나도 진다.  # 등수를 알 필요는 없기 때문에 위와 마찬가지로 기록된 경기 수가 n이라면 cnt +1  
def solution(n, results):  
    answer = 0  
  
    # 승패리스트 만들어주기    
	win = [[] for _ in range(n + 1)]  
    lose = [[] for _ in range(n + 1)]  
  
    # 주어지는 경기 결과를 패자, 승자 리스트에 추가해주기.    
	for i, j in results:  
	    win[i].append(j)  
        lose[j].append(i)  
  
        # 모든 선수 순회  
    for i in range(1, n + 1):  
        visited = [0 for _ in range(n + 1)]  
        # 방문기록 남겨주고    
		visited[i] = 1  
        # 이긴 선수 따라서 경기 매치 기록해주기    
		q = deque([i])  
        while q:  
            player = q.popleft()  
            for node in win[player]:  
                if visited[node] == 0:  
                    visited[node] = 1  
                    q.append(node)  
		# 진 선수 따라서 경기 매치 기록해주기  
        q = deque([i])  
        while q:  
            player = q.popleft()  
            for node in lose[player]:  
                if visited[node] == 0:  
                    visited[node] = 1  
                    q.append(node)  
  
        if visited.count(1) == n:  
            answer += 1  
  
    return answer

```