import sys
sys.stdin = open('input.txt')

P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}

# 암호 코드 정보 확인 (16진수 -> 2진수)
hex_to_bin = {hex(i).replace('0x', '').upper() : f'{i:04b}' for i in range(16)}

# 2진수 -> 암호코드 변환
def scanner():
    ans = 0
    # 하나의 row씩 체크하며
    for i in range(N):
        # 16진수 -> 2진수 -> 16진수의 최댓값 F는 2진수로 1111 -> 4bit
        # 인덱스 에러 방지를 위해 -1 (마지막 제외)
        j = M * 4 - 1
        # 최소 가로 길이(56 -> 마지막 55)
        while j >= 55:
            # 현재가 1이고 윗 줄이 0
            if arr[i][j] == '1' and arr[i - 1][j] == '0':
                pwd = []

                # 모든 암호코드는 8개의 숫자로 구성 -> 체크
                for _ in range(8):
                    # 암호는 (
                    # 암호 코드는 오른쪽 3개의 숫자만 봐도 됨(가장 앞은 x)
                    c2 = c3 = c4 = 0
                    # 0이면 -> 하나 앞으로
                    while arr[i][j] == '0':
                        j -= 1
                    # 1이면 -> 하나 앞으로 & c4(1개수) count += 1
                    while arr[i][j] == '1':
                        c4, j = c4 + 1, j - 1
                    # 0이면 -> 하나 앞으로 & c3(0개수) count += 1
                    while arr[i][j] == '0':
                        c3, j = c3 + 1, j - 1
                    # 1이면 -> 하나 앞으로 & c2(1개수) count += 1
                    while arr[i][j] == '1':
                        c2, j = c2 + 1, j - 1

                    # 최솟값 찾고
                    MIN = min(c2, c3, c4)
                    # 최솟값으로 나눠서 암호문에 대응하는 숫자 찾기
                    # 비율이기 때문에 가장 작은 값으로 나눠주는 과정 필요
                    pwd.append(P[(c2 // MIN, c3 // MIN, c4 // MIN)])

                # 짝수 & 홀수 자리 합
                even_digit_sum = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                odd_digit_sum = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                #  (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드가 10의 배수
                if (odd_digit_sum * 3 + even_digit_sum) % 10 == 0:
                    ans += odd_digit_sum + even_digit_sum
                    # 같은 줄 내에 다른 암호코드가 있을 수 있으므로
                    # 계속 계산
            # 한 칸 앞으로
            j -= 1
    return ans

T = int(input())
for tc in range(1, T+1):
    # N: 세로, M: 가로
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    # 16진수 -> 2진수 변환 후 배열 입력
    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]
    print(f'#{tc} {scanner()}')