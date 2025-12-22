import sys
sys.stdin = open('input.txt', 'r')
#####################################


# class Node:
#     def __init__(self, value):
#         self.root = value
#         self.left = None
#         self.right = None


def travel(now):
    global ans_a
    root = now // 2
    if root == 0:
        return
    ans += value[root]
    travel(root)


def sort_tree(idx):
    # 조건 1. 부모가 없으면 종료
    root = idx // 2
    if root == 0:
        return
    if value[root] <= value[idx]:
        return
    value[root], value[idx] = value[idx], value[root]
    sort_tree(root)


T = int(input()) # test case개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    M = N // 2
    value = [0]
    for i in range(N):
        value.append(arr[i])
        if len(value) > 2:
            sort_tree(i+1)
    ans_a = 0
    travel(N)
    # print(value)
    print(f'#{tc}', ans_a)
