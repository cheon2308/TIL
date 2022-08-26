# 0은 빈칸
# 1~100은 각기 다른 인형
# 크레인은 멈춘 위치에서 가장 위에 있는 인형을 옮긴다.
# 같은 모양 인형이 쌓인다면 펑!
# 터진 인형의 개수 반환
import sys
sys.stdin = open('input.txt')


def solution(board, moves):
    answer = 0
    # 결과 담아줄 리스트
    result = []

    for i in moves:
        for j in range(len(board)):

            # 2차원배열이라 아래로 쌓이지만 인형뽑기는 1열이 첫줄이다.
            # (열 고정, 행 움직임)으로 구해준다.
            # 또한 인형뽑기가 1부터 시작하므로 -1을 해주어야 인덱스번호와 동일하다.
            if board[j][i-1] != 0:

                # 인형이 들어있고 바구니 제일 위에 똑같은 인형이 들어있다면
                # 빼주고 +2
                if len(result) > 0 and result[-1] == board[j][i-1]:
                    result.pop()
                    answer += 2
                # 아니라면 담아준다.
                else:
                    result.append(board[j][i-1])
                # 인형뺀거 기록
                board[j][i - 1] = 0
                break



    return answer


board = [list(map(int, input().split())) for _ in range(5)]
moves = list(map(int, input().split()))

print(solution(board, moves))