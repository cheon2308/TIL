# 예약제
# N명, 0초 시작, M초에 K개
import sys
from collections import deque
import time
sys.stdin = open('input.txt')



start = time.time()
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    arrive1 = list(map(int, input().split()))

    # 기다리는 시간없이 붕어빵 제공가능 하면 possible, 아니라면 impossible
    result = 0
    # 시간 카운트
    second = 1
    # 붕어빵 주면서 q에서 빼준다.
    arrive1.sort()
    arrive = deque(arrive1)

    # 첫사람이 기다리면 바로 종료
    if arrive[0] < M:
        print(f'#{tc} Impossible')

    # 처음만들었을 때 전부 받아갈 수 있다면 종료
    elif len(arrive) < K:
        print(f'#{tc} Possible')

    # 둘 다 아니라면 카운트 세주면서 본다.
    else:
        # 빵만드는 개수보다 작게 남았다면 종료해도된다.
        while len(arrive) >= K and result == 0:
            # 사람 수만큼 반복
            for i in range(K):
                # 현재 생산 사이클보다 사람이 일찍 방문한다면
                # 현재까지 총 생산가능한 빵개수를 시간으로 표현!
                if M * second > arrive[0]:
                    result = 1
                    print(f'#{tc} Impossible')
                    break
                arrive.popleft()
            second +=1
        else:
            if result == 0:
                print(f'#{tc} Possible')

print("time :", time.time() - start)