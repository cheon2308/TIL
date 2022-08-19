import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]


    a = True
    while a:
        # 가로 체크
        for i in range(len(sudoku)):
            # 가로 세로 검증하기 위한 리스트
            number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(len(sudoku)):
                number[sudoku[i][j]-1] = 0

            for k in number:
                if k:
                    print(f'#{tc} 0')
                    a = False
                    break

            if a == False:
                break
        # 세로 체크
        for i in range(len(sudoku)):
            number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(len(sudoku)):
                number[sudoku[j][i]-1] = 0

            for k in number:
                if k:
                    print(f'#{tc} 0')
                    a = False
                    break

            if a == False:
                break
        # 3x3 체크
        for k in range(3):
            for l in range(3):
                number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(k+3):
                    for j in range(l+3):
                        number[sudoku[i][j]-1] = 0

                for k in number:
                    if k:
                        print(f'#{tc} 0')
                        a = False
                        break

            if a == False:
                break
        if a == False:
            break

        else:

            print(f'#{tc} 1')
            break


