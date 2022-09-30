# 암호 코드 8개 숫자
# (홀수 자리 합 x 3) + (짝수자리의 합) = 10의 배수
# 암호코드 1개가 포함된 직사각형 배열
# 1, 0으로만 이루어져 있고, 암호코드 이외의 부분은 전부 0
# 숫자 하나는 7개의 비트로 암호화, 따라서 가로 길이는 56


# 0 - 0001101
# 1 - 0011001
# 2 - 0010011
# 3 - 0111101
# 4 - 0100011
# 5 - 0110001
# 6 - 0101111
# 7 - 0111011
# 8 - 0110111
# 9 - 0001011
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    binary = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    # 암호가 존재하는 입력 라인 저장해주기
    password = [input() for _ in range(N) ]
    for i in password:
        if '1' in i:
            p = i
    result = []
    idx = 0

    # 뒤에서 부터 읽으면서 마지막 번호 인덱스 들고오기
    for ix, j in enumerate(p[::-1]):
        if j == '1':
            idx = ix
            break
    # 뒤집은 상태로 읽었으므로 => 전체길이 - 저장된 인덱스 = 마지막 번호
    for k in range(M-idx-56,M-idx+1, 7):
        # 7개씩 읽으면서 10진수로 변환 해준다.
        # 인덱스 번호 = 10진수 값
        for l in range(len(binary)):
            if p[k:k+7] == binary[l]:
                result.append(l)
    # print(result)



    result2 = 0
    result3 = 0
    for i in range(8):
        if i%2 == 0:
            result2+= result[i]
        else:
            result3 += result[i]

    if (result2*3 + result3 )% 10 == 0:

        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} {0}')
