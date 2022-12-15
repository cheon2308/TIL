

[백준 9663_N-Queen](https://www.acmicpc.net/problem/9663)





## 조건



- N x N 크기의 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다
- N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.







## 접근 방법



- 전형적인 백트래킹 문제이다.
- 모든 경우의 수를 살펴보는 브루트포스를 기반으로
- 이후의 사건이 이전의 사건에 종속이므로 -> 가지치기
- 재귀를 통하여 백트래킹으로 풀어준다.
- 같은 열, 대각선에 퀸이 존재하는 경우 놓을 수 없다.





#### pypy 통과 -> 백준에서는 시간이 빡빡하여 python으로는 통과가 되지 않았다.

```python
def adjacent(x): # x와 i가 같으면 행이 같은거
    for i in range(x):
        # 열이 같거나 대각선에 위치라면 false
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓아보기
        for i in range(N):
            row[x] = i
            # 행, 열 대각선 체크 true 반환시 다음 줄 체크
            # 백트래킹
            if adjacent(x):
                dfs(x+1)



N = int(input())
row = [0] * N
result = 0

dfs(0)
print(result)
```





#### 다른 분 코드 참고 -> python3 통과

- 더 많은 리스트를 선언해주고 
- 전체 케이스의 절반은 나머지 절반을 좌우대칭한 그림이랑 같다는 것을 이용하였다.
- 즉 첫행부터 -> 1 3 0 2 열에 놔두는 체스판은 2 0 3 1 열에 놔두는 체스판과 좌우 대칭 

```python
'''
전체 케이스는 col == n//2 를 중심으로 좌우대칭임

ex)
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0

0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0

때문에, col(x)가 n//2 까지만 가능한 케이스를 구한후
*2 해주면 전체 케이스에 대한 정답을 알 수 있음
또한 홀수의 경우에는 n//2 + 1 를 따로 구헤줘야함
홀수의 경우에는 상하 좌우대칭이 의미없으므로 *2 해주지 않음
'''


n = int(input())
check_row = [0 for i in range(n)]
check_leftcross = [0 for i in range(n*2)]
check_rightcross = [0 for i in range(n*2)]
ret = 0

def backtracking(cur):
    if cur==n:
        global ret
        ret += 1
        return 0
    for i in range(n):
        if check_row[i] or check_leftcross[n+cur-i] or check_rightcross[cur+i]:
            continue
        else:
            check_row[i] = 1
            check_leftcross[n+cur-i] = 1
            check_rightcross[cur+i] = 1
            backtracking(cur+1)
            check_row[i] = 0
            check_leftcross[n+cur-i] = 0
            check_rightcross[cur+i] = 0


for i in range(n//2):
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0
ret = ret*2

if n%2: #홀수일경우
    i=n//2
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0

print(ret)
```

