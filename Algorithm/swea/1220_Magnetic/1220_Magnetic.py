import sys
sys.stdin = open('input.txt')

# 푸른색 N극 붉은색 S극에 끌린다.
# 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수
# 같은색이 겹쳐있으면 1개로 본다.
# 테이블 크기 100x100
# 위쪽 N극 아래쪽 S극


for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    # 1은 N극 성질가지는 자성체 즉 붉은색
    # 2는 푸른색
    # 교착상태 카운트
    cnt = 0
    for i in range(len(table)):
        number = 0
        for j in range(len(table)):

    # 같은 열에 0,1 또는 0,2 또는 2가 위에있고 1이 아래에 있으면 떨어진다.
    # 나머지 경우 1,2 순서로 맞붙으면 교착상태 1개
    # 0을 넘어야된다.
            if table[j][i] == 1:
                number = 1

            elif table[j][i] == 2:
                if number:
                    cnt += 1
                    number = 0
                else:
                    continue



    print(f'#{tc} {cnt}')

