import sys
sys.stdin = open('input.txt')

# 저장되있는 문자열 B -> 키 한번 입력으로 타이핑
# 이미 타이핑문자 제거 x
# A와 B가 주어질 때 키를 눌러야 하는 최솟값

# 전체 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 타이핑 할 문자열, 저장되있는 단어
    target, word = map(str, input().split())
    # 타이핑 횟수
    cnt = 0
    # 단어길이
    m = len(word)
    # 인덱스
    i = 0

    while i < len(target):
        # 타깃 문자열의 i번부터 word 길이만큼 비교를 해준다.
        if target[i:i+m] == word:
            cnt +=1
            # 동일하면 +1 후 i의 인덱스를 word 길이만큼 더해준다.
            i = i+m
        else:
            # 동일하지 않다면 다음 글자로 옮겨주고 +1해준다.
            i+=1
            cnt+= 1

    print(f'#{tc} {cnt}')





import sys
sys.stdin = open('input.txt')

# # 왜 틀리는지 모르겟음
#
#
# 전체 테스트 케이스 수
T = int(input())

for tc in range(1, T + 1):

    # 타이핑 할 문자열, 저장되있는 단어
    target, word = input().split()
    # 타이핑 횟수
    cnt = 0
    i, j = 0,0

    while i < len(target):
        # 글자가 동일하다면 인덱스 1씩 이동
        if target[i] == word[j]:
            j += 1
            i += 1
            # j의 인덱스가 word의 길이와 같다면 +1 후 j인덱스 0으로 이동
            # 앞에서 동일할때 +1을 먼저 해주기 떄문에 -1이 아닌 len(word)
            if j == len(word):
                cnt+=1
                j = 0
            # word를 다 순회하지 못하고 끝난다면 그만큼 타이밍 횟수 더해준다.
            elif i == len(target):
                cnt+=j

        # 동일하지 않다면 j+1만큼 카운트 해준 후 j초기화 i+1
        # banna bana와 같이 앞의 3글자만 맞는 경우 타이핑카운트를 안올려줬으므로
        # j의 인덱스만큼 더해준 후 틀린 글자 카운트 +1을 해준다.
        else:
            cnt+= j+1
            j = 0
            i +=1


    print(f'#{tc} {cnt}')




















