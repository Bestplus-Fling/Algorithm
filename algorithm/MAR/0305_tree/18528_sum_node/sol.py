import sys
sys.stdin = open('input.txt', 'r')
#####################################


def search(node):
    global ans_a
    if node not in tree:
        ans += node
        return

    for child in tree[node]:
        search(child)
    return


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = {}

    for i in range(1, N-M+1):
        if N-M == i and i % 2 != 0:
            tree[str(i)] = [str(i*2)]
        else:
            tree[str(i)] = [str(i*2), str((i*2)+1)]

    for i in range(M):
        idx, num = input().split()
        tree[idx] = [int(num)]
    # print(tree)
    ans_a = 0
    search(str(L))
    print(f'#{tc}', ans_a)

