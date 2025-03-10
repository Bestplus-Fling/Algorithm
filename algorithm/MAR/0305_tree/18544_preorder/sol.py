import sys
sys.stdin = open('input.txt', 'r')
#####################################


# 전위 순회
def pre_order(node):
    if node not in tree:
        return

    for j in tree[node]:
        ans.append(j)
        pre_order(j)


# 정점의 총 수 V
V = int(input())
# V-1개의 간선
arr = list(map(int, input().split()))
tree = {}
# 답에 1을 미리 추가
ans = [1]
for i in range(0, len(arr), 2):
    # 부모 노드와 자식 노드를 입력
    parent, child = arr[i], arr[i + 1]
    # 자식 노드번호를 value 로 하는 딕셔너리를 생성
    # 이미 부모 노드 번호에 대한 딕셔너리가 있을 때 child 를 추가
    tree[parent] = tree.get(parent, []) + [child]
# 전위 순회 함수 호출
pre_order(1)
# 출력
print(*ans)