


이번엔 **O(N)의 시간복잡도**를 가지는 **Manacher** 알고리즘을 알아보자.

> **동작 원리**

-   우선 문자열 S에 대해 **배열 A**를 구할 수 있다.
-   배열 A는
    -   i번째 원소 A[i]는 i번째 문자를 중심으로 하는 가장 긴 회문의 반지름 크기를 의미
    -   예를들어 ban**a**nac에서 붉은색 a의 A[4]는 최대 반지름인 2가 된다.
    -   즉, 부분 문자열 S의 4 - A[4]에서 4 + A[4]까지는 팰린드롬이며, 4 - A[4] - 1에서 4 + A[4] + 1까지는 팰린드롬이 아니다. (anana는 팰린드롬이지만, bananac는 팰린드롬이 아니다.)

이를 일반화 하면 어떤 문자열 S에서 A[i]가 존재한다면, 

i - A[i]에서 i + A[i]까지는 팰린드롬이고, i - A[i] - 1에서 i + A[i] + 1까지는 팰린드롬이  아니라는 것이다.

이 과정을 이용하여 bananac라는 문자열에 대한 배열 A를 알아보자.

![](https://blog.kakaocdn.net/dn/bAfl5s/btrWUcvMQYo/Q0AkgYB5kFXA2eXYBAA9KK/img.png)

길이가 홀수인 문자열 s에 대해 다음을 O(n)에 구할 수 있다. 길이가 짝수인 문자열은 중간에 **더미문자**를 추가해준다.

dp[i] : s[i]를 중심으로 하는 가장 긴 팰린드롬의 반지름

(예를들어, s : aba  -> dp : 0 1 0)

n = s.size()

i : [0~n-1] 순서대로 초기화 할 것.

0~i-1까지 팰린드롬 중 가장 우측의 오른쪽 경계 r과 그때의 인덱스 k을 이용해서 dp[i]초기화

다음과같이 경우를 나누어 초기화해 준다.

1) i<=r 

i의 점을 k에 대해 대칭시킨 점 p. (p+i = 2*k -> p= 2*k-i)

1-1)

p를 중심으로 하는 가장 긴 팰린드롬이 k를 중심으로 하는 가장 긴 팰린드롬에 속하는 경우

dp[i] = dp[p]

1-2)

p를 중심으로 하는 가장 긴 팰린드롬이 k를 중심으로 하는 가장 긴 팰린드롬의 왼쪽으로 경계를 넘는 경우

dp[i] = i~r까지 거리 = r-i

2) i>r

while문을 이용해서 직접 찾아줘야 한다. 

i-dp[i]-1, i+dp[i]+1번째가 같은지 탐색하며 dp[i]를 1씩 올려주면 된다.

![](https://blog.kakaocdn.net/dn/buNAnw/btrWRD8SbB2/RcxOg9fj24QBeVcWgAfHLK/img.png)

```c++
string t,s;
int dp[MAX], n, r=-1, k=-1;

int main() {
	FAST; cin >> s;
		
	n = s.size();
	for (int i = 0; i < n; i++) {
		if (i <= r) dp[i] = min(r - i, dp[2 * k - i]);
		while (i - dp[i] - 1 >= 0 && i + dp[i] + 1 < n && s[i - dp[i] - 1] == s[i + dp[i] + 1])
			dp[i]++;
		if (r < i + dp[i]) r = i + dp[i], k = i;
	}
```

또는 반복문의 범위를 2*N-1로 하여 홀수 길이와 짝수 길이를 번갈아 가며 탐색해줄 수도 있다.

```python
from sys import stdin
input = stdin.readline


def solve():
    Str = input()[:-1]
    N = len(Str)
    ans = [2500] * (N + 1)
    ans[0], ans[N] = 1, 0

    # 2*N-1 인 이유: 홀수길이, 짝수길이 번갈아가며 팰린드롬 여부 확인하기 위해
    for i in range(1, 2 * N - 1):
        # i가 홀수: 짝수길이, i가 짝수: 홀수길이
        start, end = i // 2, (i + 1) // 2
        while 0 <= start and end < N:
            if Str[start] == Str[end]:
                if ans[start-1] + 1 < ans[end]:
                    ans[end] = ans[start-1] + 1
                start -= 1
                end += 1
            else: break

    return ans[N-1]


print(solve())
```