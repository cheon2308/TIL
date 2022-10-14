# N*N 크기의 절벽지대에 활주로 건설
# 각 셀의 숫자는 그 지형의 높이
# 높이가 동일한 구간에서 건설 가능
# 높이가 다르다면 활주로 끊어지기 때문에 삼각형 모양의 경사로 설치 필요

# 경사로 길이 X이고 높이 1
# 경사로는 높이 차이가 1이고 낮은 지형의 높이가 동일하게 경사로의 길이만큼 연속되는 곳에 설치 가능


# 6<=N<=20
# 경사로의 높이는 항상 1이고, X는 2이상 4이하의 정수


import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    grd = [[*map(int, input().split())] for _ in range(N)]
    cnt = 0
    # 가로 먼저 검사
    # x만큼의 길이가 필요
    # 지형의 높이는 1 이상 6 이하의 정수
    start = 0
    for i in range(N):
        start += 1
        for j in range(start, N-1):
            if grd[i][j] == grd[i][j+1]:
                continue
            # 현재 높이가 작다면 이전 높이가 경사로 설치 되는지 확인
            elif grd[i][j] < grd[i][j+1]:
                # 이전 x만큼의 길이가 범위 내이고 높이차이 1이라면
                if 0<=j-X<N and grd[i][j-X:j+1] == [grd[i][j]]*X:
                    continue
                else:
                    break
            elif grd[i][j] > grd[i][j + 1]:
                # 이전 x만큼의 길이가 범위 내이고 높이차이 1이라면
                if 0 <= j + X < N and grd[i][j:j + X + 1] == [grd[i][j]] * X:
                    continue
                else:
                    start = j+1

        else:
            cnt+=1


    # 세로 검사 하기 위해서 zip 활용
    grd2 = [list(x) for x in zip(*grd)]

    # x만큼의 길이가 필요
    # 지형의 높이는 1 이상 6 이하의 정수
    for i in range(N):
        for j in range(N - 1):
            if grd2[i][j] == grd2[i][j + 1]:
                continue
            # 현재 높이가 작다면 이전 높이가 경사로 설치 되는지 확인
            elif grd2[i][j] < grd2[i][j + 1]:
                # 이전 x만큼의 길이가 범위 내이고 높이차이 1이라면
                if 0 <= j - X < N and grd2[i][j - X:j + 1] == [grd2[i][j]] * X:
                    continue
                else:
                    break
            elif grd2[i][j] > grd2[i][j + 1]:
                # 이전 x만큼의 길이가 범위 내이고 높이차이 1이라면
                result = 0
                idx = grd
                # if
                # else:
                #     break
        else:
            cnt += 1



    print(cnt)