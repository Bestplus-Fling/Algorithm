import sys
sys.stdin = open('input.txt', 'r')
#########################################


def quick(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left_nums, right_nums = [], []
    for i in range(1, len(nums)):
        if nums[i] > pivot:
            right_nums.append(nums[i])
        else:
            left_nums.append(nums[i])
    return [*quick(left_nums)]+[pivot]+[*quick(right_nums)]
    pass


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans_a = quick(arr)
    print(f"#{tc}", ans_a[N // 2])