import sys
sys.stdin = open('input.txt')

# NxN 크기의 단어 퍼즐에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리 수

T = int(input())

for tc in range(1, T+1):
    # 단어 퍼즐의 가로,세로 길이 N
    # 단어의 길이 K
    N, K = map(int, input().split())
    # 퍼즐모양, 0이 검은 칸
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 들어갈 수 있는 자리 카운트
    cnt = 0
    # 단어길이 확인용 리스트
    check = [1] * K
    # K만큼 1이 연속되어야 한다.
    # 가로 먼저
    for i in range(N):
        for j in range(N-K+1):
            # 양끝의 경우 인덱스 에러 날 수 있으므로 따로 해준다.
            if j == 0:
                if puzzle[i][j+K] == 0 and puzzle[i][j:j+K] == check:
                    cnt +=1
            elif j == N-K:
                if puzzle[i][j-1] == 0 and puzzle[i][j:j+K] == check:
                    cnt +=1
            else:
                if puzzle[i][j+K] == 0 and puzzle[i][j-1] == 0 and puzzle[i][j:j+K] == check:
                    cnt+=1

    # 세로 구하기위해 전치행렬 새롭게 구해준다.
    new_puzzle = []
    for l in range(N):
        new_puzzle.append([puzzle[k][l] for k in range(N)])



    # 세로도 가로와 똑같이 구해준다.
    for i in range(N):
        for j in range(N - K + 1):
            # 양끝의 경우 인덱스 에러 날 수 있으므로 따로 해준다.
            if j == 0:
                if new_puzzle[i][j + K] == 0 and new_puzzle[i][j:j + K] == check:
                    cnt += 1
            elif j == N - K:
                if new_puzzle[i][j - 1] == 0 and new_puzzle[i][j:j + K] == check:
                    cnt += 1

            else:
                if new_puzzle[i][j + K] == 0 and new_puzzle[i][j - 1] == 0 and new_puzzle[i][j:j + K] == check:
                    cnt += 1

    print(f'#{tc} {cnt}')