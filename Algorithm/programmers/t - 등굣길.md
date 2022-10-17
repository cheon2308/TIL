
[프로그래머스 등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898](https://school.programmers.co.kr/learn/courses/30/lessons/42898)


## 조건

- 가장 왼쪽 위, 집의 좌표 (1,1)
- 가장 오른쪽 아래, 학교의 좌표 (m,n)
- 격자의 크기 m,n과 물이 잠긴 지역의 좌표 담은 2차원 배열 puddles가 매개변수
- 오른쪽과 아래쪽으로만 움직일 수 있으며
- 학교까지 갈 수 있는 최단 경로의 개수를 1,000,000,007로 나눈 나머지를 return 하여라





## 접근 방법

- 현재 칸에 올 수 있는 경로의 수 -> 왼쪽과 위쪽칸의 합과 같다.
- 이 때, 웅덩이를 만난다면, 경로의 수를 0으로 초기화 해준다. 
- 반복문을 줄여주기 위해서 웅덩이를 기록해주는 것이 아닌 바로바로 조건문으로 체크하기
- 또한 좌표의 값이 행열이 아닌 열과 행으로 주어지기 때문에 물 웅덩이 또한 열과 행 순서로 구해주어야 한다.


```python
def solution(m, n, puddles):
    road = [[0] * (m + 1) for _ in range(n + 1)]
    # 경로의 합 -> 왼쪽과 위의 좌표 값의 합
    # 1,1 -> 집부터 시작이므로 
    # 집은 1이여야 하므로 1,0을 1로 기록해주기
    road[1][0] = 1
    for k in range(1, n + 1):
        for l in range(1, m + 1):
            # 웅덩이 만나면 경로 수 초기화
            if [l, k] in puddles:
                road[k][l] = 0
            # 아니라면 위와 왼쪽 칸 더해주기
            else:
                road[k][l] = road[k - 1][l] + road[k][l - 1]


    return road[n][m]

```