import sys
sys.stdin = open('input.txt')

# NxN 농장 크기 항상 홀수
# 수확은 항상 농장의 크기에 맞게 마름모 형태로만 가능

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    crop = [list(map(int, input())) for _ in range(N)]

    # 첫 줄 - 가운데
    # 둘 째 - 가운데 + 양옆 1칸
    # ...  - 시작 부터 끝 - 가운데줄 기준 양 끝을 한번에 더해준다.

    value = 0
    # 한 줄당 늘어나는 칸수
    num = 0


    for i in range(len(crop)):
        for j in range(len(crop)):
            # 처음부터 끝까지 더하는 가운데줄이라면 한번만 더해주고 벗어나준다.
            if num * 2 + 1 == len(crop):
                value += crop[i][j]
            else:
                for k in range(num+1):
                # 가운데 지점이고 범위 안에 있다면
                # 첫 줄 1칸
                # 둘 쨰 3칸 - (k = -1,0,1) 이렇게 3칸
                # 셋 쨰 5칸
                    if j == (len(crop)//2) - k or j == (len(crop)//2) + k:
                        value += crop[i][j]
                        value += crop[N-i-1][j]

        # 반복문 탈출위한 조건문
        if num == len(crop)//2:
            break
        else:
            num+=1

    print(f'#{tc} {value}')