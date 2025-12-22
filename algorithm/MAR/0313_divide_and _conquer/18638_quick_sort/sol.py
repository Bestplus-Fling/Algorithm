import sys
sys.stdin = open('input.txt', 'r')
#####################################

def quick(nums):
    n = len(nums)
    if n <= 1:
        return nums
    pivot = nums[0]
    left, right = [], []
    for idx in range(1, n):
        if nums[idx] > pivot:
            right.append(nums[idx])
        else:
            left.append(nums[idx])
    return [*quick(left), pivot, *quick(right)]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    A = quick(arr)
    print(f'#{tc}', A[N//2])
