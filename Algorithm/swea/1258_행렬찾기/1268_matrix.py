import sys
sys.stdin = open('input.txt')


# 화학물질 용기 n^2개, nxn 배열
# 빈 용기 0, 들어있는 용기 1~9

# 화학물질 담긴 용기 - 사각형이고 사각형 내부에는 빈 용기 x
# 각 사각형은 차원수가 다름, 가로 세로 방향으로는 빈 용기 존재, 대각선은 없을 수 있음

# 테스트 케이스는 여러 개의 그룹 구성
T =int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 행렬 개수 및 저장
    cnt = 0
    matrix = []
    # 전체 순회하며
    for i in range(n):
        for j in range(n):
            # 세부 범위 설정
            # 행 개수저장
            row_cnt = 0
            # 시작위치 설정, 조사하지 않은 i부터
            for k in range(i, n):
                if arr[k][j] == 0:
                    break
                else:
                    # 행 개수 +1, 행렬시작
                    row_cnt += 1
                    col_cnt = 0

                for l in range(j, n):
                        if arr[k][l] == 0:
                            break
                        else:
                            col_cnt +=1
                            # 다시 조사 안하게 0으로 변경
                            arr[k][l] =0
            # 행렬이 존재한다면
            if row_cnt * col_cnt != 0:
                matrix.append([row_cnt*col_cnt, row_cnt, col_cnt])
                cnt+=1

    # 크기대로 정렬 후
    matrix.sort(key=lambda x: (x[0], x[1]))
    print(f'#{tc} {cnt}', end=' ')
    for i in range(len(matrix)):
        print(matrix[i][1], matrix[i][2], end=' ')

    print()
