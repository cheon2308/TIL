# import sys
# input = sys.stdin.readline
#
# N = int(input())
# num = list(map(int, input().split()))
# num.sort()
# M = int(input())
# target = list(map(int, input().split()))
# hash = {}
# for i in num:
#     if i in hash:
#         hash[i] +=1
#     else:
#         hash[i] = 1
#
# print(' '.join(str(hash[j]) if j in hash else '0' for j in target))


from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(C)

_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))