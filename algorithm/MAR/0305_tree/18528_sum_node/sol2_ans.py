import sys
sys.stdin = open('input.txt', 'r')
#####################################


def check(node):
    global ans
    # leaf node 를 만났을 때 node type 은 str 이므로 겹치지 않는다
    if node not in tree:
        # 합을 저장 후 return
        ans += int(node)
        return
    # 자식 노드를 호출
    for child in tree[node]:
        check(child)
    pass


T = int(input())
for tc in range(1, T+1):
    # 총 노드 수, leaf node, 시작 노드
    N, M, L = map(int, input().split())
    tree = {}
    # root 는 부모가 없으므로 고려하지 않음(패드립 아님)
    for i in range(2, N+1):
        # 부모 노드 확인
        t = i // 2
        # 자식 노드를 부모 노드의 value 에 추가
        tree[t] = tree.get(t, []) + [i]

    # leaf node 의 값을 추가, 노드 번호와 구분하기 위해 str 형태로 입력
    for i in range(M):
        idx, num = input().split()
        tree[int(idx)] = [num]
    ans = 0
    check(L)
    print(f'#{tc}', ans)
