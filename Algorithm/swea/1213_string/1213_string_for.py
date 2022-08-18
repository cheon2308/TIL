import sys
sys.stdin = open('input.txt', encoding='utf-8')

def bruteForce(pattern, target):
    count = 0
    for i in range(len(target) - len(pattern) + 1):
        for j in range(len(pattern)):
            # 두 값이 다른 경우가 나올떄 까지
            if pattern[j] != target[i+j]:
                break
        else:
            count += 1
    return count



for _ in range(10):
    tc = int(input())
    P = input()
    T = input()

    result = bruteForce(P, T)
    print(f'#{tc} {result}')
