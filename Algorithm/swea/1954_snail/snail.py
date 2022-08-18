import sys
sys.stdin = open('input.txt')

# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어짐
# N크기의 달팽이를 출력하라

# 전체 테스트 케이스 수
T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    # 변경횟수 cnt, 방향전환용 변수 dn
    cnt, dn = 1, 0
    # 현재 위치 i, j 저장
    i, j = 0, 0
    # N*N 배열 생성
    snail = [[0]*N for _ in range(N)]

    # 첫 위치에 1저장
    snail[0][0] = 1
    # N*N == cnt 일때 반복문 종료
    while cnt != N*N:
        cnt +=1
        # 이동을 위한 반복문
        while 1:
            # 방향이동
            # 해당 방향이 배열을 안 벗어나고 다른 숫자로 안 채워져있다면 이동
            if 0 <= i + di[dn] < N and 0 <= j + dj[dn] < N and snail[i+di[dn]][j+dj[dn]] == 0:
                i, j = i + di[dn], j + dj[dn]
                break
            # %4를 통해서 0~3만 바뀌도록
            else: dn = (dn+1) % 4
        # 이동한 위치에 번호 넣기
        snail[i][j] = cnt

    # 출력
    print(f'#{tc}')
    # 원소별로 불러온뒤 스페이스로
    for x in range(N):
        for y in range(N):
            print(snail[x][y], end=' ')
            #한행 끝나면 줄바꿈
        print()