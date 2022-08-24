import sys
sys.stdin = open('input.txt')

# 8개의 숫자 입력받는다
# 첫 번째 숫자 1 감소한 뒤, 맨 뒤로 이동
# 다음 수 2 감소한 뒤 맨 뒤, 그 다음 수는 3, 다음 4, 다음 5

# 이게 한 사이클

# 0보다 작아지는 경우 0유지되며 프로그램 종료, 이 때의 값이 암호

def password(minus):
    q = [] # 큐 생성
    for i in number:
        q.append(i) # 모두 큐에 넣어준다.

    # 비밀번호 생성까지 돌려준다.
    while 1:
        # 1-5까지 감소
        for j in range(1, minus+1):
            q[0] = q[0] - j
            # 만약 0이하가 된다면
            if q[0] <= 0:
                # 0으로 변경 해준 후 제일 뒤로 옮겨주고 종료
                q[0] = 0
                q.append(q.pop(0))

                return q

            # 0이 아니라면
            q.append(q.pop(0))




for tc in range(1, 11):
    N = int(input())

    number = list(map(int, input().split()))


    print(f'#{tc}', end=' ')
    for i in password(5):
        print(i, end=' ')
    print()