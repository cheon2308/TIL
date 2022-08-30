import sys
sys.stdin = open('input.txt')
import time
# 거스름돈 5만 1만 5천 천원 5백 백 5십 십
# 거슬러줄 금액 N
start = time.time()
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 거스름돈 리스트
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 인덱스 기록
    i = 0
    # 단위당 개수기록
    count = []
    while N != 0:
        # 단위보다 크다면 거슬러 준다.
        count.append(N//money[i])
        N = N % money[i]
        i+=1



    print(f'#{tc}')
    print(*count)

print(time.time() - start)

