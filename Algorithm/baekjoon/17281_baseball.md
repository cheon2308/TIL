[백준 17281_⚾](https://www.acmicpc.net/problem/17281)



## 조건 
- 총 N 이닝 동안 게임을 진행
- 한 이닝에 3아웃 발생하면 이닝 종료
	-   안타: 1
	-   2루타: 2
	-   3루타: 3
	-   홈런: 4
	-   아웃: 0
- 1번 선수는 무조건 4번 타자로 결정
- 다른 선수의 타순을 모두 결정해야 하는데 가장 많이 득점하는 타순을 찾고, 그 때의 득점을 출력
- 다음 이닝이 진행 될 때에는 직전 이닝의 마지막 타자 다음 타순부터 시작한다.




## 접근 방법
- 타순을 세우는 순열을 만들어 줄건데 1~9번이 아닌 2~9번의 타자의 타순을 정해준다.
- 이후 4번 타자로 고정되어 있는 1번 타자를 slicing을 통하여 가운데 넣어준다.
- 각 베이스 정보 리스트를 만들어주어 후속 타자의 타격 결과에 따른 조건문을 만들어 준 후
- 정보를 갱신해주며 득점 정보를 갱신해준다.
- 아웃카운트가 3개가 된다면 공수교대이므로 종료
- 파이썬 정답자가 0명.. 이므로 pypy로 제출
- 또한 현재 이닝이 끝나거나, 9->1번 타자로 돌아와야 되는 경우도 있으므로 현재 타자의 정보를 저장해주어야 한다.
- 다음 이닝은 이전 이닝의 마지막 타자 다음 순서 이므로 (hitter+1) % 9 를 이용하여 저장해주면 된다.



```python
from itertools import permutations  
import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
  
  
N = int(input())  
# 최댓값 저장  
cnt = 0  
  
hit_info = [[*map(int, input().split())] for _ in range(N)]  
  
# 2~9번 타자 순열 만들어주기  
for taja in permutations((range(1 , 9)), 8):  
    # 4번 타자는 0번인덱스 선수 고정이므로 추가해주기  
    taja = list(taja[:3]) + [0] + list(taja[3:])  
  
    # 현재 타자  
    hitter = 0  
    # 이번 이닝 점수  
    result = 0  
    for i in range(N):  
        out = 0  
        base = [0,0,0,0]  
  
        # 3아웃 까지 돌려준다.  
        while out < 3:  
            # 현재 이닝 타자 정보에서 현재 타자 불러와주기  
            hit = hit_info[i][taja[hitter]]  
  
            # 아웃, 1루, 2루, 3루, 홈런 일 때의 조건문 작성  
            if hit == 0:  
                out += 1  
  
            # 안타일 때 3루에 주자가 있다면 +1  
            # 이후 베이스 정보 갱신            
            elif hit == 1:  
                result += base[3]  
                base = [0, 1, base[1], base[2]]  
  
            # 2루타인 경우 2, 3루 주자만큼 +1  
            elif hit == 2:  
                result += base[2] + base[3]  
                base = [0, 0, 1, base[1]]  
  
            elif hit == 3:  
                result += base[1] + base[2] + base[3]  
                base = [0, 0, 0, 1]  
  
            elif hit == 4:  
                result += base[1] + base[2] + base[3] + 1  
                base = [0, 0, 0, 0]  
  
            # 다음 타자 불러오기 위해 +1 해준 후 9로 나눠주면 된다.  
            hitter = (hitter+1) % 9  
  
    if result > cnt:  
        cnt = result  
  
print(cnt)
```