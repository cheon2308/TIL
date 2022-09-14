import sys
sys.stdin = open('input.txt')

def in_order(node):
    node = int(node)
    # 해당 노드가 있는 경우에만
    if node:
        # 왼쪽 먼저 방문하고
        in_order(data[node][2])
        print(data[node][1], end='')
        # 오른쪽 방문
        in_order(data[node][3])


for tc in range(1, 11):
    N = int(input())
    data = [input().split() for _ in range(N)]

    # 노드 번호, 알파벳, L, R
    data.insert(0, [0,0,0,0])
    for i in data:
        # 자식이 없거나 하나인 경우, 크기를 맞춰준다.
        while len(i) != 4:
            i.append('0')

    print(f'#{tc}', end=' ')
    in_order(data[1][0])
    print()