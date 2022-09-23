import sys
sys.stdin = open('input.txt')


def ds(i, j, k, n):  # k는 방향, n 은 진행한 칸수
    global copy_i, copy_j, max_val
    if k == 3 and i == copy_i and j == copy_j:  # 출발점에 도착한경우
        if max_val < n:
            max_val = n
    elif i < 0 or i >= N or j < 0 or j >= N:  # 범위 밖
        return
    elif arr[i][j] in path:  # 숫자가 겹친경우
        return
    else:  # 갈 수 있는곳
        path.append(arr[i][j])
        if k == 0 or k == 1:  # 오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우에
            ds(i + di[k], j + dj[k], k, n + 1)  # 방향 그대로 쭉 가는것
            ds(i + di[k + 1], j + dj[k + 1], k + 1, n + 1)  # 방향 꺾음
        elif k == 2:
            if i + j != copy_i + copy_j:  # 출발점을 향하는게 아님 ( 도착할 수 있는 경우가 아닐 때 )
                ds(i + di[2], j + dj[2], k, n + 1)  # 그냥 쭉 가
            else:    # ( 도착할 수 있는 경우일 때 )
                ds(i + di[3], j + dj[3], k + 1, n + 1)  # 방향 꺾어서 가
        else:  # k가 3일때는 직진한다.
            ds(i + di[3], j + dj[3], k, n + 1)
        path.pop()


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = -1
    path = []
    # 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]
    for i in range(N):
        for j in range(1, N - 1):
            copy_i = i
            copy_j = j
            path.append(arr[i][j])
            ds(i + 1, j + 1, 0, 1)
            path.pop()

    print("#{} {}".format(tc, max_val))


