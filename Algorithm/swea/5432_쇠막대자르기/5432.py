import sys
sys.stdin = open('input.txt')

# 전체 테스트 케이스 수
T = int(input())

# 쇠막대 아래에서 위로 겹쳐놓고
# 레이저 위에서 수직 발사

# 쇠막대기는 자신보다 긴 쇠막대 위에만 놓일 수 있다.
# 끝점 겹치지 않게 완전히 포함
# 각 쇠막대 자르는 레이저는 적어도 하나 이상
# 레이저는 어떤 쇠막대의 양 끝점과도 겹치지 x

# 레이저 = 여는 괄호와 닫는 괄호의 인접한 쌍
# 쇠막대기 끝 (    )


for tc in range(1, T+1):
    # 쇠막대와 레이저 배치 받기
    no_cut = input()
    # 잘린 개수 카운트
    cnt_stick = 0

    # 막대의 입출력을 담아줄 리스트
    new_lst = []
    for i in range(len(no_cut)):
        # 여는 괄호 일시 추가
        if no_cut[i] == '(':
            new_lst.append('(')
        # 닫는 괄호 일시 바로 앞에 여는 괄호가 있다면 터트린 후 길이 더해준다.
        else:
            if no_cut[i-1] =='(':
                new_lst.pop()
                cnt_stick += len(new_lst)
            # 닫는 괄호 바로 앞에 닫는 괄호 인 경우 막대 한층이 끝난 것이므로 +1
            else:
                new_lst.pop()
                cnt_stick += 1

    print(f'#{tc} {cnt_stick}')
