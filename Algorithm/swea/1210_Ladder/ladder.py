import sys

sys.stdin = open('input.txt')

# 사다리타기하며 가로줄을 만나면 좌우 방향 전환 후 아래로
# 100x100 배열 이동경로 =1로 표시, 도착 2

# 총 10개의 tc
for tc in range(1, 11):
    N = int(input())
    # 100x100 배열 사다리 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 현재위치 저장
    x = 0
    y = 0
    # 먼저 도착지점부터 찾고 올라온다.
    for i in ladder[99]:
        if i == 2:
            y = 99
            break
        x += 1

    # 올라가다가 왼쪽 혹은 오른쪽 값이 1이라면 방향전환
    while 1:
        # y=0이면 출발점에 도착했기 때문에 break
        if y == 0:
            break
        # 좌측에 사다리가 있다면 좌회전
        if 0 <= x - 1 < 100 and ladder[y][x - 1] == 1:
            x -= 1
        # 우측에 사다리가 있다면 우회전
        elif 0 <= x + 1 < 100 and ladder[y][x + 1] == 1:
            x += 1
        # 좌우에 없다면 위로 이동
        else:
            y -= 1
        # 온 길 돌아가지 않기 위해 다른값으로 변경해준다.
        ladder[y][x] = 0

    print(f'#{tc} {x}')