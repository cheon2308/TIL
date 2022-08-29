import sys
sys.stdin = open('input.txt')

# 스프레이 한 번에 최다 킬
# 노즐은 +형태라 + 또는 x로만 분사
# M의 세기에 따라 M칸 파리
# N의 크기, 세기는 칸을 벗어나도 상관없다.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 파리 리스트 받아주고
    fly = [list(map(int, input().split())) for _ in range(N)]
    # 최다킬
    max_kill =0
    # 전체 리스트 돌며
    for i in range(len(fly)):
        for j in range(len(fly)):
            # 한번 뿌렸을 때의 킬 기록
            kill = 0
            # 중심부제외 이므로 M의 세기 +1해준다.
            for k in range(i-M, i+M+1):
                for l in range(j-M, j+M+1):
                    # 범위 초과라면 그냥패스

                    if k<0 or k>=N:
                        break
                    elif l < 0 or l >= N:
                        continue
                    # 벗어나지 않는다면 +모양으로 더해준다.
                    #elif 0<=k<N and 0<=l<N:
                    else:
                        # print(type(k), type(i), k, i)
                        # 가로 더해주기
                        if i == k:
                            kill += fly[i][l]

                        # 세로 더해주기
                        elif j != l:
                            #print(k, i)
                            kill += fly[k][j]

            if kill>max_kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')