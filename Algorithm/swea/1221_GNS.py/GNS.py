import sys
sys.stdin = open('input.txt', encoding='UTF-8')


# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 입력받은 문자열을 크기대로 정렬하라
T = int(input())

for tc in range(1, T+1):
    # 테스트케이스번화와 길이 출력
    N, M = map(str, input().split())
    # 테스트 케이스 단어 리스트 생성
    st_num = list(map(str, input().split()))
    # 순서대로 출력할 딕셔너리 생성
    dict_num = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    # 입력받은 단어 리스트를 키로 사용하여 해당하는 밸류값 +1 씩 해준다.
    for i in range(len(st_num)):
        dict_num[st_num[i]] += 1

    new_lst = []
    # 키 * 밸류값을 통하여 작은 수부터 차례대로 정렬하는데 ' '을 이용하여 공백으로 구분해준다.
    for j in dict_num:
        new_lst.append((j+' ')*dict_num[j])
    # 리스트를 문자열로 바꿔준다.
    result = ''.join(new_lst)

    print(f'#{tc}')
    print(f'{result}')

