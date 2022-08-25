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

    # 행렬 크기 기록해줄 시작, 끝 인덱스 기록 변수
    sti, stj = -1, -1
    endi, endj = -1, -1
    # 행렬 개수
    cnt = 0
    di = []
    dj = []
    xy = []
    # 상하좌우 탐색 계수
    dn = 0
    while 1:
        for i in range(sti,len(arr)):
            for j in range(len(arr)):
                if arr[i][j] != 0:
                    sti, stj = i, j
                    break
            if sti > -1 and stj > -1:
                break

        for k in range(sti+1, len(arr)):
            if arr[k][stj] == 0:
                endi = k-1
                break
        for l in range(stj+1, len(arr)):
            if arr[endi][l] == 0:
                endj = l-1
                break

        if sti>-1 and stj>-1 and endi>-1 and endj>-1:
            x = endi - sti +1
            y = endj - stj +1

            xy = x*y