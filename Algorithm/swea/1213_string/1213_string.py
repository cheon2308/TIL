import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 문자열 개수 반환 프로그램 작성
def BruteForce(word, sentence):
    N = len(word)
    M = len(sentence)
    # word의 인덱스
    i = 0
    # sentence의 인덱스
    j = 0
    cnt = 0 # 개수 반환
    while i < N and j < M:
        if sentence[j] != word[i] :
            j = j - i # 시작위치 다음 글자로 변경
            i = -1 # 시작위치로 이동 (인덱스[0]로 돌아가기 위한 작업)
        i += 1
        j += 1
        # word의 인덱스가 길이와 같다면 +1 해준 후 다시 처음으로 돌아간다.
        if i == N:
            cnt += 1
            i = 0

    return cnt # 검색 개수



# 총 10개의 테스트 케이스



for tc in range(1, 11):
    N = input()
    print(f'#{tc} {BruteForce(input(), input())}')