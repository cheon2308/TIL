import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 패턴 내의 패턴에 대한 정보를 생성하기 위함
def make_lps(p):
    # 중계 리스트
    lps = [0] * len(p)

    # lps를 위한 prefix의 index
    j = 0
    # 전체 순회는
    for i in  range(1, len(p)):
        # prefix와 suffix가 같을 때
        if p[j] == p[i]:
            lps[i] = j+1
            j +=1
        # 다르면, j를 0으로 초기화
        # pattern의 첫 글자와 다시 비교하도록 만들어야 한다.

        # 현재 순회중인 자리 (i)와 0번째로 돌아간 pattern이
        # 또 다시 일치하는지 확인

        else:
            j=0
            if p[i] == p[j]:
                lps[i] = j+1
                j+=1
    return lps

def KMP(pattern, target):
    lps = make_lps(pattern)

    # 조사 시작은 brute force와 동일하게 시작
    p_idx, t_idx = 0,0
    count = 0
    while t_idx < len(target):
        if pattern[p_idx] == target[t_idx]:
            t_idx += 1
            p_idx += 1
        else:
            # p_idx가 0이 아니라면
            if p_idx != 0:
                # lps를 써서 다음 조사 대상 수색
                p_idx = lps[p_idx - 1]
            # p_idx == 0 이라면
            # t_idx를 한 칸 증가시켜서
            # pattern의 첫번째 글자와 다음 target 조사 대상이랑 비교
            else:
                t_idx += 1

        if p_idx == len(pattern):
            count += 1
            p_idx = 0

    return count

for _ in range(10):
    tc = int(input())
    P = input()
    T = input()

    result = KMP(P,T)
    print(f'#{tc} {result}')