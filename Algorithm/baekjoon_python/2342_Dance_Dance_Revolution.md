
[백준 2342_Dance Dance Revolution](https://www.acmicpc.net/problem/2342)

#### 시간 제한 2초, 메모리 제한 128MB

## # 조건

- DDR은 아래의 그림과 같은 모양의 발판이 있고, 주어진 스텝에 맞춰 나가는 게임이다. 
- 발판은 하나의 중점을 기준으로 위, 아래, 왼쪽, 오른쪽으로 연결되어 있다. 
	- 편의상 중점을 0, 위를 1, 왼쪽을 2, 아래를 3, 오른쪽을 4라고 정하자.

![](assets/Pasted%20image%2020230319152954.png)
- 처음에 게이머는 두 발을 중앙에 모으고 있다.(그림에서 0의 위치) 
- 그리고 게임이 시작하면, 지시에 따라 왼쪽 또는 오른쪽 발을 움직인다. 하지만 그의 두 발이 동시에 움직이지는 않는다.
- 이 게임에는 이상한 규칙이 더 있다. 
	- 두 발이 같은 지점에 있는 것이 허락되지 않는 것이다. (물론 게임 시작시에는 예외이다) 
	- 만약, 한 발이 1의 위치에 있고, 다른 한 발이 3의 위치에 있을 때, 3을 연속으로 눌러야 한다면, 3의 위치에 있는 발로 반복해야 눌러야 한다는 것이다.
- 오랫동안 DDR을 해 온 백승환은 발이 움직이는 위치에 따라서 드는 힘이 다르다는 것을 알게 되었다. 
- 만약, 중앙에 있던 발이 다른 지점으로 움직일 때, 2의 힘을 사용하게 된다. 그리고 다른 지점에서 인접한 지점으로 움직일 때는 3의 힘을 사용하게 된다. (예를 들면 왼쪽에서 위나 아래로 이동할 때의 이야기이다.) 
- 그리고 반대편으로 움직일때는 4의 힘을 사용하게 된다. (위쪽에서 아래쪽으로, 또는 오른쪽에서 왼쪽으로). 
- 만약 같은 지점을 한번 더 누른다면, 그때는 1의 힘을 사용하게 된다.

- 만약 1 → 2 → 2 → 4를 눌러야 한다고 가정해 보자. 당신의 두 발은 처음에 (point 0, point 0)에 위치하여 있을 것이다. 
- 그리고 (0, 0) → (0, 1) → (2, 1) → (2, 1) → (2, 4)로 이동하면, 당신은 8의 힘을 사용하게 된다. 다른 방법으로 발을 움직이려고 해도, 당신은 8의 힘보다 더 적게 힘을 사용해서 1 → 2 → 2 → 4를 누를 수는 없을 것이다.


#### 입력

- 입력은 지시 사항으로 이루어진다. 
- 각각의 지시 사항은 하나의 수열로 이루어진다. 
- 각각의 수열은 1, 2, 3, 4의 숫자들로 이루어지고, 이 숫자들은 각각의 방향을 나타낸다. 
- 그리고 0은 수열의 마지막을 의미한다. 
- 즉, 입력 파일의 마지막에는 0이 입력된다. 입력되는 수열의 길이는 100,000을 넘지 않는다.


## # 접근 방법

- 발의 위치를 0, 1, 2, 3, 4 로 기록해준다.
- 이제 점화식을 세우는 것이 관건인데 왼발과 오른발을 모두 고려하여야하고, 각 발이 마지막으로 누른 위치에 따라 다음 위치를 누를 때 추가되는 점수가 다른 점에서
- **왼발과 오른발 각각이 마지막으로 누른 버튼위치에 따른 점수를 기록**하면 된다.
- 그래서 dp테이블은 다음과 같이 구성하였고
	- **dp[현재 스탭 인덱스][왼발최종위치][오른발최종위치]**
- 점화식은 다음과 같이 구성하였다.
- **dp[현재 스탭 인덱스][왼발최종위치][오른발최종위치] =** **dp[직전 스탭 인덱스][왼발최종위치][오른발최종위치] + 이동하여 버튼을 누르는데 든 힘**

만약 1을 누를 차례라면
- **dp[현재스탭인덱스][1][직전 오른발최종위치]**
- **dp[현재스탭인덱스][직전 왼발최종위치][1]**

이 두가지를 각각 구하여 저장해두면 된다.

- 5번 반복 하는 이유 ->  직전 단계의 모든 경우의 수를 고려하는 것
- 즉, 처음에는 왼발 또는 오른발 2가지 경우의 수 -> 이후 왼발에 대해 2개, 오른발에 대해 2개 총 4개 -> 8개 이렇게 경우의 수가 늘어나는 것을
	- 왼발의 모든 위치와 오른발의 모든 위치로 기록해놓는 것
	- 따라서, 왼발 오른발이 같은 위치에 존재하는 경우도 생기지만 이 경우 최소가 될 수 없으므로 고려하지 않아도 된다.

```python

import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
INF = float('inf')  
  
def dist(cur, next):  
    if cur == next:  
        return 1  
    elif cur == 0:  
        return 2  
    elif abs(cur-next) % 2 == 0:  
        return 4  
    else:  
        return 3  
  
inst = [*map(int, input().split())]  
# dp [n번째 움직임][왼발 위치][오른발 위치]  
# 0, 1, 2, 3, 4가 있으므로 5의 크기로 생성  
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(inst) +1)]  
dp[0][0][0] = 0  
  
for i in range(1, len(inst)):  
    move = inst[i-1]  
    for left in range(5):  
        for right in range(5):  
            # 왼발 움직이고 오른발 고정  
            dp[i][move][right] = min(dp[i][move][right], dp[i-1][left][right] + dist(left, move))  
            # 오른발 움직이고 왼발 고정  
            dp[i][left][move] = min(dp[i][left][move], dp[i-1][left][right] + dist(right, move))  
  
result = INF  
for i in range(5):  
    for j in range(5):  
        result = min(result, dp[len(inst) -1 ][i][j])  
print(result)  
print(dp)
```


#### 다른 사람 풀이

```python

import sys  
from collections import defaultdict  
input = sys.stdin.readline  
  
order = list(map(int, input().split()))  
score = [defaultdict(list) for _ in range(len(order)-1)]  
  
n = 0  
  
while True:  
    # 종료  
    if order[n] == 0:  
        break  
  
    # 처음 / 두 발이 0에 있을 때  
    # 발: (0, order[0])  
    if n == 0:  
        score[n][0] = 2  
  
    else:  
        # 발: (key, order[n-1])  
        for key in score[n-1].keys():  
            # 한 발이 0에 있을 때  
            if key == 0:  
                # 나머지 발 order[n-1]이 눌러야 될 발판 order[n]에 있을 때  
                # 발: (0, order[n])  
                if order[n-1] == order[n]:  
                    if key in score[n].keys():  
                        score[n][key] = min(score[n][key], score[n-1][key] + 1)  
                    else:  
                        score[n][key] = score[n-1][key] + 1  
  
                # 나머지 발 order[n-1]이 눌러야 될 발판 order[n]에 없을 때  
                else:  
                    # 나머지 발 order[n-1]로 order[n]을 밟을 때  
                    # 발: (0, order[n])  
                    if key in score[n].keys():  
                        if order[n] + order[n - 1] == 4 or order[n] + order[n - 1] == 6:  
                            score[n][key] = min(score[n][key], score[n - 1][key] + 4)  
                        else:  
                            score[n][key] = min(score[n][key], score[n - 1][key] + 3)  
                    else:  
                        if order[n] + order[n - 1] == 4 or order[n] + order[n - 1] == 6:  
                            score[n][key] = score[n - 1][key] + 4  
                        else:  
                            score[n][key] = score[n - 1][key] + 3  
  
                    # 0에 있는 발로 order[n]을 밟을 때  
                    # 발: (order[n-1], order[n])  
                    if order[n - 1] in score[n].keys():  
                        score[n][order[n - 1]] = min(score[n][order[n - 1]], score[n - 1][key] + 2)  
                    else:  
                        score[n][order[n - 1]] = score[n - 1][key] + 2  
  
            # 한 발이 밟아야 하는 발판 order[n]에 있을 때  
            # 발: (order[n], order[n-1])  
            elif key == order[n]:  
                if order[n-1] in score[n].keys():  
                    score[n][order[n-1]] = min(score[n][order[n-1]], score[n - 1][key] + 1)  
                else:  
                    score[n][order[n-1]] = score[n - 1][key] + 1  
  
            # 한 발이 밟아야 하는 발판 order[n]에 있을 때  
            # 발: (key, order[n-1])  
            elif order[n] == order[n-1]:  
                if key in score[n].keys():  
                    score[n][key] = min(score[n][key], score[n - 1][key] + 1)  
                else:  
                    score[n][key] = score[n - 1][key] + 1  
  
            # 두 발 모두 0에 없고, 밟아야 하는 발판 order[n]에 없을 때  
            else:  
                # order[n-1]에 있는 발로 order[n]을 밟을 때  
                # 발: (key, order[n])  
                if key in score[n].keys():  
                    if order[n] + order[n-1] == 4 or order[n] + order[n-1] == 6:  
                        score[n][key] = min(score[n][key], score[n-1][key] + 4)  
                    else:  
                        score[n][key] = min(score[n][key], score[n-1][key] + 3)  
  
                else:  
                    if order[n] + order[n-1] == 4 or order[n] + order[n-1] == 6:  
                        score[n][key] = score[n - 1][key] + 4  
                    else:  
                        score[n][key] = score[n - 1][key] + 3  
  
                # key에 있는 발로 order[n]을 밟을 때  
                # 발: (order[n], order[n-1])  
                if order[n-1] in score[n].keys():  
                    if order[n] + key == 4 or order[n] + key == 6:  
                        score[n][order[n-1]] = min(score[n][order[n-1]], score[n - 1][key] + 4)  
                    else:  
                        score[n][order[n-1]] = min(score[n][order[n-1]], score[n - 1][key] + 3)  
  
                else:  
                    if order[n] + key == 4 or order[n] + key == 6:  
                        score[n][order[n-1]] = score[n - 1][key] + 4  
                    else:  
                        score[n][order[n-1]] = score[n - 1][key] + 3  
  
    n += 1  
  
if len(order) == 1:  
    print(0)  
else:  
    print(min(score[n-1].values()))  
  
  
print(score)
```
