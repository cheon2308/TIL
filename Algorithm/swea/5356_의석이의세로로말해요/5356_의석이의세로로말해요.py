# 장난감에 있는 글자들은 영어 A-Z, a-z, 0-9
# 수평으로 일렬로 붙여서 단어
# 그 아래쪽에 글자들을 붙여서 또 다른 단어 다섯개의 단어를 만든다.
# 세로로 읽을껀데, 위에서 아래로 첫 열부터 5열까지 공백없이 붙여서 출력


# queue를 이용해서 빼줘도 되고, 인덱스 기록해줘도 되는데 뺴주자.
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    q1 = input()
    q2 = input()
    q3 = input()
    q4 = input()
    q5 = input()


    print(f'#{tc}', end=' ')
    for i in range(15):
        if i < len(q1):
            print(q1[i], end='')
            #q1.pop(0)
        if i < len(q2):
            print(q2[i], end='')
            #q2.pop(0)
        if i < len(q3):
            print(q3[i], end='')
            #q3.pop(0)
        if i < len(q4):
            print(q4[i], end='')
           # q4.pop(0)
        if i < len(q5):
            print(q5[i], end='')
            #q5.pop(0)

    print()