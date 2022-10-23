
[프로그래머스 숫자 게임](https://school.programmers.co.kr/learn/courses/30/lessons/12987)



## 조건 

- 2 x N명의 사원들은 N명씩 두 팀으로 나눠 숫자 게임
- 먼저 모든 사원이 무작위로 자연수를 부여받고
- 각 사원은 딱 한 번씩 경기
- 각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개
- 숫자가 큰 쪽이 승리하게 되고 승리한 사원의 팀이 승점 1점
- B팀이 얻을 수 있는 최대 승점



## 접근 방법 및 Solution


- 순열을 이용하여 구해줄 수 있을 것 같지만 런타임에러가 발생할 것 같다.


```python
from itertools import permutations  
def solution(A, B):  
  
    player = list(permutations(B, len(B)))  
    result = 0  
  
    for k in player:  
        print(k)  
        cnt = 0  
        for i in range(len(A)):  
            if k[i] > A[i]:  
                cnt += 1  
        if cnt > result:  
            result = cnt  
    return result
```


- 역시나 시간 초과
- 따라서, 조금은 greedy하게 접근을 해주어야 할 것 같다.
- A, B를 모두 오름차순 시켜준 후 
- B의 인덱스를 조절해주며 A의 숫자와 비교해준다.
- 만약 B의 값이 더 크다면 A와 B 모두의 인덱스를 증가
- 그렇지 않다면 B만 증가

```python
def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()

    idx = 0
    for i in A:
        while idx < len(B):
            if B[idx] > i:
                answer += 1
                idx += 1
                break
            # 작다면 B의 idx만 1을 추가.
            idx += 1
    
    return answer
```