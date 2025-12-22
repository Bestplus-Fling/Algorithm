import sys
sys.stdin = open('input.txt', 'r')
#####################################


def stack():
    stk = []
    for t in range(N):
        if stk and int(nums[t]) == int(stk[-1]):
            stk.pop()
            continue
        stk.append(nums[t])

    return ''.join(stk)


T = 10
for tc in range(1, T+1):
    N, nums = input().split()
    N = int(N)
    print(f'#{tc}', stack())
