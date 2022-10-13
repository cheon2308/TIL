[백준 17626_Four Squares](www.acmicpc.net/problem/17626)



## 조건
- 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다.
- 어떤 자연수는 복수의 방법으로 표현
- 예 - 26 = 5^2 + 1^2 or 4^2 + 3^2 + 1^2
- 자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 프로그램 작성
- 시간 제한 - 0.5초
- 1<=n<=50,000




## 접근 방법
- n만큼의 인덱스를 가진 dp 테이블을 만들어준다.
- 2에서 n+1까지 반복문을 돌려주는데 
- min_value는 4로 잡아주고 , j= 1부터 시작해준다.
- 반복문 내에서 while문을 활용하여 j^2이 현재 결과값 i보다 작을 때만 while문 동작
- while 문 내부에서는 i-j^2 인 수의 dp 테이블 값을 들고 와준다.
- 이후 최솟값과 현재값을 비교하며 갱신
- dp[i]의 값은 최소값 +1을 해주어야 한다.




#### pypy제출

```python
n = int(input())  
n_list = [0]*(n+1)  
n_list[1] = 1  
for i in range(2,n+1):  
    j = 1  
    min_v = 4  
    while((j**2)<=i):  
        min_v = min(min_v,n_list[i-(j**2)])  
        j+=1  
    n_list[i] = min_v+1    
print(n_list[n])
```





### python 다른 분 코드 참고 

#### 1. 길이가 2, 3개로 이루어진 중복 조합 구하여서 더하기

```python
from itertools import combinations_with_replacement as comb

n = int(input())
nums = list(i*i for i in range(1, 224))
if n in nums:
    print(1)
elif n in list(map(sum, comb(nums, 2))):
    print(2)
elif n in list(map(sum, comb(nums, 3))):
    print(3)
else:
    print(4)
```


#### 2. brute force 이용

- 제곱근이 정수일 때
- 제곱근 - i의 제곱근이 정수 일 때
- 제곱근 - i의 제곱근 - j의 제곱근이 정수 일 때를 구해준다.

```python
import math
 
def fourSquares(n):
    # √n이 정수일 때
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    # √(n - i^2)이 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2
    # √(n - i^2 - j^2)이 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
    # 남은 경우는 4
    return 4
 
 
n = int(input())
print(fourSquares(n))
```
