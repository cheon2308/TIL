**CCW(Counter Clock Wise)** 알고리즘은

- **벡터의 외적**을 통해 세 점의 위치 관계가 시계방향인지 아닌지 판별하는 알고리즘이다.

> **선분 교차 판별**

- ccw 알고리즘을 이용하여 선분 교차를 판별할 수 있다.
- 한 선분을 기준으로 **같은 방향에 위치**할 경우 **선분은 교차되지 않고** **그렇지 않은 경우 교차**한다.

![](https://blog.kakaocdn.net/dn/kGuAI/btr4v7V3zRE/9PSjkdcabIYRUazioGVXZK/img.png)

즉, ccw 함수의 수행 결과로 **반시계 방향이 1, 시계 방향의 -1**을 갖는다면 CCW(A, B, C)의 결과와 CCW(A, B, D) 결과의 곱이 -1 이 되는 경우 **서로 다른 방향에 위치**하게 된다.

다만, 아래와 같이 같은 방향이어도 교차하지 않는 경우가 있다. 

![](https://blog.kakaocdn.net/dn/6bKtY/btr4voDLtHk/NUzZLUAlZKSfaiJMpK4gB0/img.png)

- 이 경우는 선분 CD 에 대해서도 CCW 알고리즘을 수행하여 판별한다.
- 또한, 평행인 경우도 존재하므로, 조건을 잘 분기해주어야 한다.

![](https://blog.kakaocdn.net/dn/B2Ie0/btr4zdA5zyY/3zk37yb8Zkgqt4PyJKoDO1/img.png)

- 신발끈 공식을 이용하여 풀어줄 수 있다.

#### 참고문제

[http://www.acmicpc.net/problem/11758](http://www.acmicpc.net/problem/11758)

첫째 줄에 P1의 (x1, y1), 둘째 줄에 P2의 (x2, y2), 셋째 줄에 P3의 (x3, y3)가 주어진다. (-10,000 ≤ x1, y1, x2, y2, x3, y3 ≤ 10,000) 모든 좌표는 정수이다. P1, P2, P3의 좌표는 서로 다르다.

```python
dot = []
for i in range(3):
    dot.append(list(map(int, input().split())))

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

result = ccw(dot[0], dot[1], dot[2])
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
```