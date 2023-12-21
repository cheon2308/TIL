
[백준 21939 - 문제 추천 시스템 Version 1](https://www.acmicpc.net/problem/21939)

#### **시간 제한 1초, 메모리 제한 512MB**

## **# 조건**

- Tony9402는 최근 깃헙에 코딩테스트 대비 문제를 직접 뽑아서 "**문제 번호**, **난이도**"로 정리해놨다.
- 깃헙을 이용하여 공부하시는 분들을 위해 새로운 기능을 추가해보려고 한다.
- 만들려고 하는 명령어는 총 3가지가 있다. 
	- 아래 표는 각 명령어에 대한 설명이다.

|   |   |
|---|---|
|**recommend $x$**|$x$가 1인 경우 추천 문제 리스트에서 가장 어려운 문제의 번호를 출력한다.<br><br>만약 가장 어려운 문제가 여러 개라면 문제 번호가 큰 것으로 출력한다.<br><br> $x$가 -1인 경우 추천 문제 리스트에서 가장 쉬운 문제의 번호를 출력한다.<br><br>만약 가장 쉬운 문제가 여러 개라면 문제 번호가 작은 것으로 출력한다.|
|**add $P$ $L$**|추천 문제 리스트에 난이도가 $L$인 문제 번호 $P$를 추가한다. (추천 문제 리스트에 없는 문제 번호 $P$만 입력으로 주어진다. 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도로 다시 들어 올 수 있다.)|
|**solved $P$**|추천 문제 리스트에서 문제 번호 $P$를 제거한다. (추천 문제 리스트에 있는 문제 번호 $P$만 입력으로 주어진다.)|

- 명령어 **recommend**는 추천 문제 리스트에 문제가 하나 이상 있을 때만 주어진다.
- 명령어 **solved**는 추천 문제 리스트에 문제 번호가 하나 이상 있을 때만 주어진다.
- 위 명령어들을 수행하는 추천 시스템을 만들어보자.

#### **입력**
- 첫 번째 줄에 추천 문제 리스트에 있는 문제의 개수 $N$ 가 주어진다.
- 두 번째 줄부터 $N + 1$ 줄까지 문제 번호 $P$와 난이도 $L$가 공백으로 구분되어 주어진다.
- $N + 2$줄은 입력될 명령문의 개수 $M$이 주어진다.
- 그 다음줄부터 $M$개의 위에서 설명한 명령문이 입력된다.

#### **출력**
- **recommend 명령이 주어질** 때마다 문제 번호를 한 줄씩 출력한다. 
- 최소 한번의 recommend 명령어가 들어온다.

#### **제한**
- 1<=N, P<=100,000
- 1<=M<=10,000
- 1<=L<=100, L은 자연수
- x =  (+-1)

## **# 접근 방법**

- `recommand` 명령어의 종류에 따라 최소 난이도와 최대 난이도를 뽑아야 하므로 **최소 힙과 최대 힙**을 활용해주면 된다.
	- 파이썬의 경우 **최소 힙만을 지원**하므로 난이도와 문제 번호에 -를 붙여 넣어주면 된다.
- 처음엔 set를 활용하여 추천 문제 번호만 기록하려고 했지만, 같은 번호의 다른 난이도가 들어올 수 있으므로 dictionary를 이용해준다.
- 문제를 풀었다면 딕셔너리에서 -1로 변경해주고 recommand 시에는 현재 힙의 0번 인덱스의 문제 번호의 난이도가
	- 딕셔너리에 기록되어 있는 난이도와 같을 때까지 pop을 해준다.

```python

import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
from heapq import heappop, heappush  
from collections import defaultdict  
  
N = int(input())  
problems = defaultdict(int)  
min_q = []  
max_q = []  
  
for _ in range(N):  
    # 문제 난이도, 번호로 heapqpush  
    # 최소 힙만 지원하므로    # 최대 힙의 경우 - 를 붙여 넣어주어야 한다.    
    a, b = map(int, input().split())  
    heappush(min_q, (b, a))  
    heappush(max_q, (-b, -a))  
    problems[a] = b  
  
M = int(input())  
for _ in range(M):  
    query = list(input().strip().split())  
    if len(query) == 2:  
        q1, q2 = query[0], int(query[1])  
    else:  
        q1, q2, q3 = query[0], int(query[1]), int(query[2])  
    if q1 == 'add':  
        heappush(min_q, (q3, q2))  
        heappush(max_q, (-q3, -q2))  
        problems[q2] = q3  
    elif q1 == 'solved':  
        problems[q2] = -1  
    else:  
        if q2 == 1:  
            while not problems[abs(max_q[0][1])] == abs(max_q[0][0]):  
                heappop(max_q)  
            print(abs(max_q[0][1]))  
        else:  
            while not problems[min_q[0][1]] == min_q[0][0]:  
                heappop(min_q)  
            print(min_q[0][1])
```