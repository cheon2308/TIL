import sys
from collections import deque
sys.stdin = open('input.txt')

# 비상연락망과 연락을 시작하는 당번에 대한 정보가 주어진다.
# 가장 나중에 연락을 받게 되는 사람의 번호는?
# 마지막에 동시에 여러 명이 연락 받는다면 가장 큰 숫자 출력


# bfs 이용하면 될듯
def bfs(start):
    # 방문기록 남겨주고 시작위치 1로 변경 및 q에 담아준다.
    global visited
    visited = [0] * (101)
    visited[start] = 1
    q = deque()
    q.append(start)
    cnt = 0
    while q:
        # 시작 위치에서 탐색시작
        s = q.popleft()
        for i in range(len(contact[s])):
            # 연락할 사람이 있고 아직 안했다면 q에 넣어주고 visited +1 해준다.
            if contact[s][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[s] +1

    return visited

for tc in range(1, 11):
    # 연락 인원, 당번
    N, start = map(int, input().split())
    # 연락 관계 입력해줄 리스트 - 최대 100명이니 101로 만들어준다
    contact = [[0]*(101) for _ in range(101)]
    arr = list(map(int, input().split()))
    # a -> b 형식으로 주어지므로 a행의 b열에 1을 남겨서 찾아갈 수 있게 해준다.
    # print(arr)
    for i in range(0, len(arr)-1,2):
        contact[arr[i]][arr[i+1]] = 1
    # print(contact[2])

    bfs(start)

    # 방문 리스트를 받아와 최대값 추출한후
    # 리스트에서 찾아서 인덱스값 기록해준다.
    # 어짜피 연락번호=인덱스이므로 가장 마지막 번호 추출
    a = max(visited)
    for i in range(len(visited)):
        if visited[i] == a:
            result = i

    print(f'#{tc} {result}')

