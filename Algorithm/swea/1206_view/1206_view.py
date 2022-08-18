import sys
sys.stdin = open('input.txt')



# 전체 테스트 케이스 수


for tc in range(10):
    num = int(input())
    window = list(map(int, input().split()))
    result = 0  # 조망권 확보한 집의 총 수
    # 가장 왼쪽 2칸, 오른쪽 2칸은 0이므로 3번째 집부터 테이스케이스 길이 -2 만큼 반복해준다
    for j in range(2, num-2):
        # 테이스 케이스가 5칸 내에서 가장 높다면
        if window[j] > window[j-2] and window[j] > window[j-1] and window[j] > window[j+1] and window[j] > window[j+2]:
            # 2번째로 높은 층을 구해서 빼준다.
            if window[j-2] >= window[j-1] and window[j-2] >= window[j+1] and window[j-2] >= window[j+2]:
                result += (window[j] - window[j-2])
            elif window[j-1] >= window[j-2] and window[j-1] >= window[j+1] and window[j-1] >= window[j+2]:
                result += (window[j] - window[j-1])
            elif window[j+1] >= window[j-2] and window[j+1] >= window[j-1] and window[j+1] >= window[j+2]:
                result += (window[j] - window[j+1])
            elif window[j+2] >= window[j-2] and window[j+2] >= window[j-1] and window[j+2] >= window[j+1]:
                result += (window[j] - window[j+2])
    print(f'#{tc+1} {result}')