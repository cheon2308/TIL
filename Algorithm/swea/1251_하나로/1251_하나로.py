import sys
sys.stdin = open('input.txt')

# N개의 섬들을 연결하는 교통시스템 설계 프로젝트인 '하나로'
# 모든 섬을 해저터널로 연결
# 시작 섬부터 n-1의 모든 섬에 갈 수 있으면 연결 된 것
# 세율 E와 각 해저터널 길이 L의 제곱의 곱 (E*L^2)만큼 지불
# N개의 모든 섬을 최소 환경 부담금으로 설계

def prim(r,V):
    # MST 포함여부
    MST = [0]*V
    MST[r] = 1
    s = 0
    # V개의 정점 중 V-1개를 선택
    for _ in range(V-1):
        u = 0
        minV = float('inf')
        # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
        for i in range(V):
            if MST[i] == 1:
                for j in range(V):
                    if money[i][j] > 0 and MST[j] == 0 and minV>money[i][j]:
                        u = j
                        minV = money[i][j]
        s += minV
        MST[u] =1
    return s

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    island = [[] for i in range(N)]

    for i in range(N):
        # 각 섬의 x좌표, y표 합쳐주기
        island[i] =([x[i],y[i]])
    # 세금
    E = float(input())

    money = [[0]*N for _ in range(N)]
    # 거리에 따른 세금 계산해주기
    # 두점 사이의 거리
    # (a to b)^2 = (ax-bx)^2 + (ay-by)^2
    for i in range(N):
        for j in range(N):
            # 두점 사이의 거리 ^2 * 세율
            money[i][j] = (((island[i][0]-island[j][0])**2) + ((island[i][1]-island[j][1])**2))*E



    print(f'#{tc} {int(round(prim(0,N),0))}')
