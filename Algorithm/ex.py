import sys
sys.stdin = open('input.txt')

N = int(input())
node = [0]*N
child= list(map(int, input().split()))
for i in range(N):
	node[i] = int(input())

erase = int(input())
print(node)