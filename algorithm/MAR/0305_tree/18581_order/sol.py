import sys
sys.stdin = open('input.txt', 'r')
#####################################

# 전위 순회
def pre_order(node):
    # 먼저 root를 추가
    ans_a[0].append(node)
    # 최하위 노드라면 return
    if node not in tree:
        return
    # 나머지 자식 노드를 L -> R 순서로 추가
    for ch in tree[node]:
        pre_order(ch)

# 중위 순회
def in_order(node):
    # 최하위 노드인 경우 리스트에 추가, return
    if node not in tree:
        ans_a[1].append(node)
        return

    # L 자식 call
    in_order(tree[node][0])
    # root 추가
    ans_a[1].append(node)
    # R 자식이 있을 때만 call
    if len(tree[node]) > 1:
        in_order(tree[node][1])

# 후위 순회
def post_order(node):
    # 최하위 노드인 경우 리스트에 추가, return
    if node not in tree:
        ans_a[2].append(node)
        return
    # L -> R -> root 순으로 추가
    post_order(tree[node][0])
    # R 자식이 있을 때만 call
    if len(tree[node]) > 1:
        post_order(tree[node][1])
    ans_a[2].append(node)


# 정점의 총 수 V
V = int(input())
# V-1개의 간선 입력
arr = list(map(int, input().split()))
tree = {}
# 최종 출력을 저장하는 리스트 생성
ans_a = [[] for _ in range(3)]

for i in range(0, len(arr), 2):
    # 부모 노드 번호와 자식 노드 번호를 입력받는다.
    parent, child = arr[i], arr[i + 1]
    # 딕셔러니에 부모 노드 번호를 key 로 하는 딕셔너리를 생성
    # 이미 생성된 부모 노드가 있다면 child 를 추가
    tree[parent] = tree.get(parent, []) + [child]
# print(tree)
# 전위, 중위, 후위 순으로 함수 호출
pre_order(1)
in_order(1)
post_order(1)

for i in range(3):
    print(*ans_a[i])
