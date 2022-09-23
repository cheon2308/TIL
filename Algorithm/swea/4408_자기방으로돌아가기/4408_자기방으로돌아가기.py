# 최단 시간에 모든 학생이 자신의 방으로 돌아가려 한다.
# 숙소는 긴 복도를 따라 총 400 개의 방이 존재
# 1 3 5 ----- 399
# 2 4 6 ----- 400

# 겹친다면 동시에 못돌아간다.

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    student = [list(map(int, input().split())) for _ in range(N)]

    # 이동시 +1씩 해준다.
    # 최댓값 = 걸리는 시간
    room = [0] * 201
    for sti, end in student:
        if sti < end:
            # 1번과 2번의 복도는 0번이라 생각
            # 따라서 짝수인 경우 -1, 홀수인 경우 그대로
            # 도착 지점의 경우 +1을 해주므로 짝수인 경우 도착//2와 같다.

            # 둘다 홀수인 경우, 시작//2부터 도착//2에 도착해야하므로 +1해주어야 한다.
            if sti%2 and end%2:
                for j in range(sti//2, end//2+1):
                    room[j] +=1
            elif sti % 2:
                for j in range(sti // 2, end // 2):
                    room[j] += 1
            elif end%2:
                for j in range(sti//2-1, end//2+1):
                    room[j] +=1
            else:
                for j in range(sti // 2 - 1, end // 2 ):
                    room[j] += 1



        # 400 -> 1과 같이 큰 번호 방에서 작은 번호 방으로 가는 경우
        elif sti > end:
            if sti % 2 and end % 2:
                for j in range(end // 2, sti // 2 + 1):
                    room[j] += 1
            # 홀수는 그대로 짝수는 -1해준다.
            elif sti % 2:
                for j in range(end // 2-1, sti // 2+1):
                    room[j] += 1
            elif end % 2:
                for j in range(end // 2 , sti // 2 ):
                    room[j] += 1
            else:
                for j in range(end // 2 -1, sti // 2):
                    room[j] += 1


    print(f'#{tc} {max(room)}')

