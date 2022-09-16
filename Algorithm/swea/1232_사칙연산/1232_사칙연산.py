import sys
sys.stdin = open('input.txt')
# 1
# 전위순회
def inord(nd):
    # 숫자면 숫자 출력
    if tr[nd].isnumeric(): return int(tr[nd])
    # 사칙연산이면 좌우 노드 값의 연산
    if tr[nd] == '+': return inord(chd[nd][0]) + inord(chd[nd][1])
    if tr[nd] == '-': return inord(chd[nd][0]) - inord(chd[nd][1])
    if tr[nd] == '*': return inord(chd[nd][0]) * inord(chd[nd][1])
    # 남은 경우가 나누기 밖에 없으니 그냥 return
    return inord(chd[nd][0]) / inord(chd[nd][1])

for t in range(1, 11):
    n = int(input())
    tr = ['']*(n+1)
    chd = [[] for _ in range(n+1)]
    for _ in range(n):
        a = list(input().split())
        # tr 안에는 연산자/숫자 넣음
        tr[int(a[0])] = a[1]
        # chd에 자식 노드 간선 정보 저장
        # 연산이기 때문에 무조건 양쪽 노드가 존재
        if len(a) == 4:
            chd[int(a[0])] = [int(a[2]),int(a[3])]
    # print(chd)
    # print(tr)
    # 전위노드로 계산
    rst = int(inord(1))
    print(f'#{t} {rst}')

# 2

import sys
sys.stdin = open('input.txt')

# 후위 순회
def postorder(node):
    if len(arr[node]) == 2:
        return arr[node][1]
    else:
        l = postorder(arr[node][2])
        r = postorder(arr[node][3])

        if arr[node][1] == '+':
            return l + r
        elif arr[node][1] == '-':
            return l - r
        elif arr[node][1] == '*':
            return l * r
        else:
            return l // r

for tc in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    for data in arr:
        i = 0
        # 연산을 위해 모든 10진수 정수로 변경
        while i < len(data):
            if data[i].isdecimal():
                data[i] = int(data[i])
            i += 1
    # node 번호가 1부터 시작 -> 0은 사용하지 않음
    arr.insert(0, 0)
    print(f'#{tc} {postorder(1)}')