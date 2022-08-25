# N개의 막대 기둥, 폭은 1m 높이는 다를 수 있음
# 지붕은 모두 연결되어야하고, 수평부분은 반드시 기둥의 윗면과 닿아야함
# 수직은 기둥의 옆면과 닿아야함
# 가장자리는 땅에 닿아야하고 지붕의 어떤 부분도 오목하게 들어가지 않는다.


# 기둥 개수
N = int(input())
# 기둥 왼쪽면 L, 높이 H
pillar = []
length = 0
for i in range(N):
    a, b = map(int, input().split())
    pillar.append((a, b))
    if a > length:
        length = a
# 기둥 왼쪽면 기준 정렬
pillar.sort()

#print(pillar)
sum = 0
start = 0
while start < length :
    for j in range(start+1, length):
        # 오른쪽 기둥 높이가 왼쪽보다 낮다면 지나간다.
        if pillar[j][1] < pillar[j-1][1]:
            continue
        # 그렇지 않다면 창고넓이 계산 후 시작 지점 바꿔준다.
        else:
            sum += (pillar[j][0] - pillar[j-1][0]) * pillar[j-1][1]
            start = pillar[j][0]
            break

print(sum)