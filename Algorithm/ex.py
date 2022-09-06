import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 앞의 상자가 작다면 뒤의 상자에 넣을 수 있다.
# ex 1 5 2 3 7 의 경우 1-> 5,  2 -> 3 -> 7이라면 한번에 넣을 수 있는 최대 수는 3이지만
# 1 -> 2-> 3-> 7 이 된다면 4개를 넣을 수 있다.



N = int(input())
box  = list(map(int, input().split()))


print(box)
