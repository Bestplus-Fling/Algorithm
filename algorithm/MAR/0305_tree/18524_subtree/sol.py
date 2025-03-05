import sys
sys.stdin = open('input.txt', 'r')
#####################################


def search(node):
    global ans
    # 최하위 노드 check
    if node not in tree:
        ans += 1
        return
    # 자식 노드가 있을 때 리스트를 순회, 재귀함수 호출
    for ch in tree[node]:
        search(ch)
    # 자기 자신을 포함해서 count
    ans += 1


T = int(input()) # test case개수를 받아오는 코드
for tc in range(1, T+1):
    # E: 전체 간선 수, N: 노드 시작점
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = {}

    # 딕셔너리에 부모 노드 번호를 key로 하고 자식들의 묶음을 value로 하는 딕셔너리 생성
    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]
        tree[parent] = tree.get(parent, []) + [child]

    ans = 0
    search(N)
    # print(tree)
    print(f"#{tc}", ans)
