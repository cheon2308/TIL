
### **LCS (Longest Common Subsequence) 란?**

-   2개 이상의 문자열에서 공통으로 나타나는 부분 문자열 중 가장 긴 문자열을 의미
-   대표적으로 DNA의 공통 염기서열을 찾아 데이터를 압축하거나
-   무선 서명을 통해 휴대폰에서 사용자를 인증할 때 사용

> **풀이 방법**

-   분할정복이 아닌 **DP**를 이용하여 풀이해준다.

#### **1. Top-down 방법 (재귀적 풀이)**

문자열 X, Y 가 X = [x1, x2, x3, .... , xm], Y = [y1, y2, y3, ... , yn] 일 때, 아래와 같은 과정을 반복한다.

```
LCS(X, Y): #수열 X와 Y의 최장 공통 부분 수열(LCS)의 길이
    m, n = len(X), len(Y)
    if m == 0 or n == 0:
        return 0
    else:
    	if X[-1] == Y[-1]:
            return LCS(X[:m-1], Y[:n-1]) + 1
        else:
            return max(LCS(X, Y[:n-1]), LCS(X[:m-1], Y))
```

-   재귀적으로 LCS를 해결할 경우 하나의 값을 여러 번 호출하기 때문에 중복되는 부분 문제가 발생
-   따라서, **O(2^n)** 시간복잡도를 가진다.

![](https://blog.kakaocdn.net/dn/bHGqtx/btrTyEwvF6b/6Oy7rOsdYjjRkSNGTp6zv0/img.png)

https://osnim.tistory.com/entry/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-LCSLongest-Common-Subsequence-%ED%8C%8C%EC%9D%B4%EC%8D%AC

### **2. Bottom-Up 방식 (dp 풀이)**

-   Top-down 방식과 반대로 하여 중복 부분 문제는 한번만 계산하도록 바꿔 시간복잡도를 낮춰준다.

![](https://blog.kakaocdn.net/dn/yERzw/btrTyEccNUG/QJsMKQp24t6cb5cMkJtSfK/img.png)

https://osnim.tistory.com/entry/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-LCSLongest-Common-Subsequence-%ED%8C%8C%EC%9D%B4%EC%8D%AC

![](https://blog.kakaocdn.net/dn/Q0MEP/btrTvj7q6Jx/IeZiZnu8HmUhLntbLSg1H0/img.png)

위와 같이 길이에 맞는 2차원 배열을 생성해준다.

이후 첫 문자 C는 ACAYKP에 있으므로 아래와 같이 1로 표시해주는데, 

최장 공통 부분 수열은 똑같이 C이므로 나머지도 1로 표시

![](https://blog.kakaocdn.net/dn/cIGAMy/btrTvjsVnG5/vCXwlkQkGB6Ffiq5pPHkY0/img.png)

![](https://blog.kakaocdn.net/dn/tZUc7/btrTxIlzmvg/JoMzSHMWKwkrCWjyA3Exv0/img.png)

이렇게 계속 채워준다.

```PYTHON
def LCS(X, Y):
    X, Y = " " + X, " " + Y 
    for i in range(1, len(X)-1):
        for j in range(1, len(Y)-1):
            if X[i] == Y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
```

#### **역추적 이용 -> LCS 구하기**

-   LCS의 길이가 아닌 LCS를 구하고 싶으면 백트래킹을 하여야 한다.
-   dp[n][m]에서 시작
-   arr[i] == arr[j] 이고 dp[i][j] = max이면 dp[i-1][j-1]로 이동한다. 
-   그리고 max -1
-   만약, dp[i-1][j] = dp[i][j] 이면 dp[i-1][j] 로 이동하고,
-   dp[i][j-1] == dp[i][j]이면 dp[i][j-1]로 이동한다.

![](https://blog.kakaocdn.net/dn/cXPap7/btrTA7c9fzR/KXziMgFU9kYbYNEFySmlKk/img.png)

```
def findit():  
    ans = ''  
    now = dp[-1][-1]  
    y = len(dp) - 1  
    x = len(dp[0]) - 1  
  
    while now != 0:  
        if dp[y][x - 1] == now - 1 and now - 1 == dp[y - 1][x]:  
            ans = a[x - 1] + ans  
            now -= 1  
            y -= 1  
            x -= 1  
        else:  
            if dp[y - 1][x] > dp[y][x - 1]:  
                y -= 1  
            else:  
                x -= 1  
    return ans
```

참고 

- [https://osnim.tistory.com/entry/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-LCSLongest-Common-Subsequence-%ED%8C%8C%EC%9D%B4%EC%8D%AC](https://osnim.tistory.com/entry/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-LCSLongest-Common-Subsequence-%ED%8C%8C%EC%9D%B4%EC%8D%AC)

 [최장 공통 부분수열, LCS(Longest Common Subsequence) (파이썬)

LCS (Longest Common Subsequence)이란? 2개 이상의 문자열에서에서 공통으로 나타나는 부분 문자열 중 가장 긴 문자열을 의미합니다. LCS은 대표적으로 DNA의 공통 염기서열을 찾아 데이터를 압축하거나

osnim.tistory.com](https://osnim.tistory.com/entry/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-LCSLongest-Common-Subsequence-%ED%8C%8C%EC%9D%B4%EC%8D%AC)

- [https://propercoding.tistory.com/8](https://propercoding.tistory.com/8)

 [[알고리즘] LCS (최장 공통 부분 수열)

목차 LCS란? LCS는 Longest Common Subsequence의 약자이다. 말 그대로 가장 긴 공통된 부분 수열이다. LCS는 보통 주어진 두 수열에서 각각의 부분 수열들 중, 서로 같은 부분 수열 중에서 가장 긴 부분 수

propercoding.tistory.com](https://propercoding.tistory.com/8)