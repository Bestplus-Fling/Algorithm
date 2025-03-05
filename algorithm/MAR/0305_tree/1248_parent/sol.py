import sys
sys.stdin = open('input.txt', 'r')
#####################################
"""
1. 모든 경우를 순회, 이 때 상위 간선 중 가장 큰 값을 저장
1-1, 완전 탐색 가능한 함수1 
2. 저장된 부모 노드부터 순회하면서 서브트리의 크기를 확인
"""


def search(node):
    global temp, flag
    # 서브트리 크기 즉정
    temp += 1
    # 공통 조상 확인되면 +1
    if node == sch1 or node == sch2:
        flag += 1
    # leaf node일 경우 리턴
    if node not in tree:
        return
    # 모든 하위 노드 순회
    for ch in tree[node]:
        search(ch)


T = int(input())
for tc in range(1, T+1):
    # V: 정점의 개수(최대 10000), E: 간선의 개수, sch1, sch2: 공통 조상을 찾는 정점 번호
    V, E, sch1, sch2 = map(int, input().split())
    # E개의 간선 입력
    arr = list(map(int, input().split()))
    tree = {}
    # 입력을 원하는 형태로 변환(dict)
    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]
        tree.setdefault(parent, []).append(child)

    # 가장 가까운 공통 조상 노드 번호, 서브트리의 크기 저장
    ans, count = 0, float('inf')
    for i in range(1, V+1):
        # print(i)
        # 서브트리 크기 임시 저장, 공통 조상을 찾았을 때의 flag
        temp, flag = 0, 0
        search(i)
        # 공통 조상을 찾았고, 서브트리 크기가 가장 작다는게 가장 가까운 조상이라는 의미
        if flag == 2 and count > temp:
            ans = i
            count = temp

    print(f'#{tc}', ans, count)