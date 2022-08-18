import sys
sys.stdin = open('input.txt')

# 높은 곳의 상자 -> 낮은 곳
# 평탄화 수행하고나면 가장 높은 곳과 가장 낮은 곳 차이 = 1이내
# 상자 옮기는 횟수 제한
# 가로 길이 100, 상자위치 1이상 100이하, 덤프 횟수 1이상 1000이하


# 테스트 케이스 10개 반복하며 수행
for tc in range(10):
    dump = int(input())
    block = list(map(int, input().split()))

    # 덤프 횟수만큼만 반복
    num = 0
    while num != dump+1:
        # 가장 높이 쌓인 박스의 숫자와 인덱스, 가장 낮게 쌓인 박스의 숫자와 인덱스 기록할 변수들
        max_box = 0
        max_floor = 0
        min_box = 101
        min_floor = 0
        # 가로의 길이는 100이므로 덤프 1번 할때마다 가장 높이 쌓인 박스와 그 인덱스
        # 가장 낮게 쌓인 박스와 그 인덱스를 저장해준다.

        # 덤프횟수 +1
        num += 1
        for i in range(100):
            if block[i] >= max_box:
                max_box = block[i]
                max_idx = i
            if block[i] <= min_box:
                min_box = block[i]
                min_idx = i
        # 가장 높이 쌓인 박스에서 1개를 가장 낮은 박스로 주기 때문에 각각 +1과 -1을 해준다.

        block[max_idx] -= 1
        block[min_idx] += 1
        # 평탄화를 한 후에 가장 높고 낮다는 보장이 없으므로 다시 찾아준다.
        for i in range(100):
            if block[i] >= max_box:
                max_box = block[i]
                max_floor = i
            if block[i] <= min_box:
                min_box = block[i]
                min_floor = i

    result = max_box-min_box
    print(f'#{tc+1} {result}')