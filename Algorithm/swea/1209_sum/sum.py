import sys
sys.stdin = open('input.txt')

# 전체 테스트 케이스수 10

for tc in range(1, 11):
    # 배열 크기 100x100 동일
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 합의 최댓값 저장
    max_arr = 0
    # 대각선 합
    arr_sum3 = 0
    # 역 대각선 합
    arr_sum4 = 0
    for i in range(100):
        # 가로 줄 합
        arr_sum1 = 0
        # 세로 줄 합
        arr_sum2 = 0

        for j in range(100):
            # 가로줄 덧셈
            arr_sum1 += arr[i][j]
            # 세로줄 덧셈
            arr_sum2 += arr[j][i]
            # 정 대각선 덧셈
            if i == j:
                arr_sum3 += arr[i][j]
            # 역 대각선 덧셈
            # 역 대각선 x,y의 합은 전체길이와 같다
            if i+j == 99:
                arr_sum4 += arr[i][j]
        if max_arr < arr_sum1:
            max_arr = arr_sum1

        if max_arr < arr_sum2:
            max_arr = arr_sum2

    if max_arr < arr_sum3:
        max_arr = arr_sum3

    if max_arr < arr_sum4:
        max_arr = arr_sum4

    print(f'#{N} {max_arr}')