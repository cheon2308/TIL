import sys
sys.stdin = open('input.txt')

# 반복된 문자 s를 지운다. 지워진 부분은 다시 앞뒤를 연결하는데,
# 만약 연결에 의해 또 반복문자가 생기면 다시 지운다.
# 반복문자 지운 후 남은 문자열의 길이
# ex) CAAABBA에서 AA지우고 C와 A를 잇는다.
# CABBA 연속문자 BB를 지우고 A와 A를 잇는다.
# CAA 연속 문자 AA를 지운다.


# 전체 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    for i in range(len(word)):
        # 입력받은 글자가 stack에 없다면 삽입해준다.
        if not word[i] in stack:
            stack.append(word[i])
        # 만약 stack에 있는데 top글자가 삽입하려는 글자와 같다면 stack의 top글자를 삭제한다.
        else:
            if word[i] == stack[-1]:
                stack.pop()
            # top글자와 같지않다면 stack에 추가해준다.
            else:
                stack.append(word[i])

    print(f'#{tc} {len(stack)}')


























# 교수님 풀이
# T = int(input())
#
# for tc in range(1, T + 1):
#     stack = []
#     word = input()
#
#     # chars의 원소를 stack에 넣음
#     for char in word:
#         # stack이 비었으면
#         if not stack:
#             stack.append(char)
#         # stack의 길이가 0이 아니면
#         # 스택의 가장 뒤 원소가 char랑 같으면 중복되므로 삭제
#         elif stack[-1] == char:
#             stack.pop()
#         # 아니라면 append
#         else:
#             stack.append(char)
#     result = len(stack)
#
#     print(f'#{tc} {result}')