from collections import Counter

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    check = Counter(nums)
    result = []
    for i in range(N*2):
        val = nums[i] * 4 / 3
        if val in check and check[val] > 0 and check[nums[i]] > 0:
            result.append(int(nums[i]))
            check[val] -= 1
            check[nums[i]] -= 1

    print(f'#{tc} ', end = '')
    result.sort()
    for r in result:
        print(r, end=' ')
    print()