import sys
T = int(input())

word = set(sys.stdin.readline().strip() for _ in range(T))
word = list(word)
# 단어 순서로 정렬
word.sort()
# 전체 길이로 정렬
word.sort(key=len)




# 단어 한 줄씩 출력
for i in word:
    print(i)