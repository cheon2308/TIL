import sys
sys.stdin = open('input.txt')

# 일반, 광역, 급행
# 정류장 1-1000번
# A번에서 B번까지 운행, A와 B에서는 반드시 정차
# 일반 버스 A-B 모든 정류장 정차
# 급행 A가 짝수인 경우, A와 B의 짝수, 홀수인경우 A와 B사이 홀수
# 광역 짝수인 경우, 4의 배수, 홀수인 경우 3의 배수이면서 10의 배수 아닌 곳
# 최대 몇 개 노선이 같은 정류장 정차

T = int(input())
for tc in range(1, T+1):
    # 노선 N
    N = int(input())
    # N개 줄 동안 버스 타입(1 일반, 2 급행, 3 광역), 출발 정류장, 도착 정류장


    bus_stop = [0] * 1001 # 기록 편하게 0번도 만들어준다.
    for i in range(N):
        bus = list(map(int, input().split()))
        if bus[1] == 0 or bus[2] == 0:
            continue
        bus_stop[bus[1]] +=1
        bus_stop[bus[2]] +=1
        if bus[0] == 1:
            for j in range(bus[1]+1, bus[2]):
                bus_stop[j] +=1
        elif bus[0] == 2:
            for k in range(bus[1]+1, bus[2]):
                if bus[1] %2 ==0:
                    if k %2 == 0:
                        bus_stop[k] +=1
                elif bus[1] %2 == 1:
                    if k % 2 == 1:
                        bus_stop[k] += 1
        else:
            for l in range(bus[1]+1, bus[2]):
                if bus[1] % 2 == 0:
                    if l % 4 == 0:
                        bus_stop[l] +=1
                elif bus[1] %2 == 1:
                    if l%3 == 0 and (not l%10 == 0):
                        bus_stop[l] +=1

    print(f'#{tc} {max(bus_stop)}')