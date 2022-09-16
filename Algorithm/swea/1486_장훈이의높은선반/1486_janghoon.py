from itertools import combinations
import sys
sys.stdin = open('input.txt')

# 높이 B인 선반, N명의 점원들의 키는 Hi
# 탑을 쌓아서 키보다 높이 있는 물건 꺼낼수 있다.
# 높이가 b이상 중 가장 낮은 탑의 높이와 b의 차이

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    a = list(map(int, input().split()))
    # 나올수 없는 제일 큰수를 min값으로 잡아준다.
    result = 200001
    for i in range(1, N+1):
        # 1~N개로 이루어진 조합을 person에 담아주며
        person = list(combinations(a, i))

        for j in person:
            # 문제 조건의 B보다 조합의 합이 크다면
            if sum(j) >= B:
                # 그때의 차이가 min값 보다 작다면 재설정해준다.
                if sum(j)-B < result:
                    result = sum(j)-B

    print(f'#{tc} {result}')
