import sys
sys.stdin = open('1267.txt', 'r')
#####################################


def dfs(node, depth):
    depths[node] = depth

    for child in tree[node]:
        # 부모 노드도 저장해야 한다.
        parents[child] = node
        dfs(child, depth+1)

    subtree[node] = 1
    for child in tree[node]:
        subtree[node] += subtree[child]


def lca(a, b):
    while depths[a] != depths[b]:
        # a가 더 깊으면 부모 노드로 이동해서 올라간다
        if depths[a] > depths[b]:
            a = parents[a]
        else:
            b = parents[b]
    # 깊이가 일치한 상태에서 부모가 다르면 서로의 부모를 불러서 비교
    while a != b:
        a = parents[a]
        b = parents[b]
    # 같아진 부모를 반환
    return a


T = 10
for tc in range(1, T+1):
    v_cnt, e_cnt, a_vertex, b_vertex = map(int, input().split())
    edges = list(map(int, input().split()))

    tree = [[] for _ in range(v_cnt + 1)]
    for i in range(e_cnt):
        tree[edges[i*2]].append(edges[i*2+1])

    # 각 노드의 부모 노드 저장
    parents = [0] * (v_cnt + 1)
    # 각 노드의 깊이 저장
    depths = [0] * (v_cnt + 1)
    # 각 노드의 서브트리 개수를 저장
    subtree = [0] * (v_cnt + 1)

    # root node (1), 깊이(0)
    dfs(1, 0)

    res = lca(a_vertex, b_vertex)

    print(f'#{tc}', res, subtree[res])