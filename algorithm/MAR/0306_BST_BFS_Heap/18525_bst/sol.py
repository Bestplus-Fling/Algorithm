import sys
sys.stdin = open('input.txt', 'r')
#####################################


def inorder(root):
    global num
    if root not in tree:
        tree_value[root] = num
        num += 1
        return
    inorder(tree[root][0])
    tree_value[root] = num
    num += 1
    if len(tree[root]) > 1:
        inorder(tree[root][1])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = {}
    for i in range(1, N+1):
        left, right = i * 2, (i * 2) + 1
        temp = []
        if left <= N:
            temp.append(left)
        if right <= N:
            temp.append(right)
        tree.setdefault(i, []).extend(temp)
        if left == N or right == N:
            break
    tree_value = [0] * (N+1)
    num = 1
    # print(tree)
    inorder(1)
    print(f'#{tc}', tree_value[1], tree_value[N//2])
