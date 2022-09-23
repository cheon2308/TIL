# 연속된 N일 동안의 물건의 매매가를 예측
# 하루에 최대 1만큼 구입 가능
# 판매는 얼마든지 가능
# 3일동안 매매가 1,2,3 이라면 처음 두날 구매하여 마지막날 팔면 3의 이득
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    # 앞에서부터 순회하면 시간초과
    # 뒤에서부터 바로바로 이익을 구해주고, max값을 변경해준다.
    max_value = price[-1]
    # 차익
    result = 0
    for i in range(N-2, -1, -1):
        # 이후 날짜동안 오늘이 최고값이라면
        if price[i] > max_value:
            # 사놓은 물건이 있다면
            max_value = price[i]
        else:
            result += max_value - price[i]


    print(f'#{tc} {str(result)}')