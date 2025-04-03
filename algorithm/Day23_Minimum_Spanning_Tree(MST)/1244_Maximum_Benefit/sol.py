import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    nums, time = list(input().split())
    N = len(nums)
    nums = list(map(int, nums))
    time = int(time)
    t, Flag = 0, True
    while t < time:
        if not Flag:
            a, b = -1, -2
            for i in range(N-1):
                if nums[i] == nums[i+1]:
                    a, b = i, i+1
                    break
            print(a, b)
            nums[a], nums[b] = nums[b], nums[a]
            t += 1
            continue
        else:
            for i in range(N):
                print(nums)
                if time <= t:
                    break
                max_val = nums[i]
                idx = i
                for j in range(N-1, i, -1):
                    if max_val < nums[j]:
                        idx = j
                        max_val = nums[j]
                if i != idx:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    t += 1
            else:
                Flag = False

    print(*nums, sep='')
