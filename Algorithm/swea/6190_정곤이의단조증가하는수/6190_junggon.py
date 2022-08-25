import sys
sys.stdin = open('input.txt')

# 각 숫자의 자리가 단순하게 증가
# k자리의 숫자가 d1<=d2<= ... <=dk 는 단조 증가 수

# 양의 정수 N개
# 1 <= i <= j <= N 일 때, Ai x Aj값이 단조 증가인 수를 구하고 그중 최댓값 출력
# 없다면 -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    max_num = 0
    for i in range(len(num)):
        # i가 j보다 작거나 같다면
        for j in range(i+1, len(num)):
            # 앞의 숫자 저장 변수
            pre_num = 0
            # 곱을 문자형식으로 저장해준다(순회위해)
            a = str(num[i] * num[j])
            for k in range(len(a)):
                # 곱을 순회하며 뒷글자가 앞글자보다 크거나 같다면
                if int(a[k])>= pre_num:
                    pre_num = int(a[k])
                    # 마지막까지 같다면
                    if k == len(a)-1:
                        # max곱과 비교하여 출력
                        if max_num < int(a):
                            max_num = int(a)
                else:
                    break
    if max_num == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_num}')

    # # 시간초과
    # # 곱을 구해서 리스트에 넣어준다.
    # for i in range(len(num)):
    #     for j in range(len(num)):
    #         if i != j:
    #             danjo.append(num[i]*num[j])
    #
    #
    # for k in danjo:
    #     # 비교 숫자 정해주고
    #     dan_num = 0
    #     # 이전 숫자보다 크거나 같지 않다면 종료
    #     for l in range(len(str(k))):
    #         if int(str(k)[l]) >= dan_num:
    #             dan_num = int(str(k)[l])
    #             if l == len(str(k)) -1 and max_num < k:
    #                 max_num = k
    #         else:
    #             break
    # print(f'#{tc} {max_num}')
