import sys
sys.stdin = open('input.txt')

# 폭 1m , 길이 2m 서로 평행 또는 직각
# 1m x 1m 해상도의 구조물은 1

# 해상도 NxM, 구조물 있으면 1, 없으면 0
# 직선인 구조물만 고려

T = int(input())
for tc in range(1, T+1):
    # N개 줄에 M개 데이터
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(N)]

    max_cnt = 0
    # data 돌아 다니며 줄 체크
    for i in range(N):
        for j in range(M):
            # 데이터 존재한다면
            if data[i][j] == 1:
                cnt = 1
                # 오른쪽 체크
                for k in range(j+1, M):
                    if data[i][k] ==1:
                        cnt+=1
                    else:
                        break
                if cnt > max_cnt:
                    max_cnt = cnt

                cnt = 1
                # 아래쪽 체크
                for l in range(i+1, N):
                    if data[l][j] ==1:
                        cnt += 1
                    else:
                        break
                if cnt > max_cnt:
                    max_cnt = cnt

    print(f'#{tc} {max_cnt}')