for tc in range(1, int(input())+1):
    answer = ''
    print(f'#{tc}')
    for _ in range(int(input())):
        alpha, n = input().split()
        n = int(n)
        answer += alpha*n
    for i in range(0, len(answer), 10):
        print(answer[i:i+10])