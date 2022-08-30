# A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B
#

N = list(map(int, input().split()))
#
result = (sum(i**2 for i in N))
#
print(result%10)