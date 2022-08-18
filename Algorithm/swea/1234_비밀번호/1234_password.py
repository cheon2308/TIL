import sys
sys.stdin = open('input.txt')

# 0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들 소거
# 번호 쌍이 소거되고 소거된 번호쌍의 좌우번호가 같은 번호이면 또 소거



for tc in range(1, 11):
    # 반복문 순회 위해 문자열로 받아준다.
    N, number = map(str, input().split())
    # 스택으로 구현
    password = []
    # 다음 숫자부터 반복문
    for i in range(len(number)):
        # 비밀번호 리스트가 비지 않았고
        if password:
            # 입력하려는 번호가 마지막 번호와 같다면 pop
            if number[i] == password[-1]:
                password.pop()
            # 같지 않다면 삽입
            else:
                password.append(number[i])
        # 비밀번호 리스트가 비어있다면 삽입해준다.
        else:
            password.append(number[i])

    result = ''.join(password)
    print(f'#{tc} {result}')

