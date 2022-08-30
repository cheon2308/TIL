import sys
sys.stdin = open('input.txt')

# 수강생 N명
# 1-N번, 제출하지 않은 학생 오름차순

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 전체 학생 리스트
    student = [0]*(N+1)
    # 제출 번호 리스트
    submit = list(map(int, input().split()))
    # 제출한 학생만 체크
    for i in range(K):
        student[submit[i]] = 1
    result = ''
    for j in range(1, len(student)):
        if student[j] == 0:
            result += str(j) + ' '

    print(f'#{tc} {result[:-1]}')

