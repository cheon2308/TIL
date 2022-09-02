import sys
sys.stdin = open('input.txt')
K, N = map(int, input().split())

cable = []
for i in range(K):
    # 가지고 있는 케이블 길이 받아준다.
    cable.append(int(input()))

# 시작, 끝, 중간점을 설정해준 후, 시작점과 끝점이 같을 때까지 실행 해주면 최대 길이 얻을 수 있다.
start = 1
end = max(cable)

while end >= start:
    middle = (end + start) // 2
    count = 0
    for i in cable:
        # 중간값으로 나눠 준 선 개수 기록
        count += i//middle
    # 만들고자 하는 개수보다 많다면 길이 +1 , 아니라면 -1
    if count >= N:
        start = middle + 1
    elif count < N:
        end = middle - 1

print(end)