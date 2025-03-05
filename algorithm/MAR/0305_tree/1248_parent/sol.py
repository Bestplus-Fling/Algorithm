import sys
sys.stdin = open('input.txt', 'r')
#####################################
"""
1. 모든 경우를 순회, 이 때 상위 간선 중 가장 큰 값을 저장
1-1, 완전 탐색 가능한 함수1 
2. 저장된 부모 노드부터 순회하면서 서브트리의 크기를 확인
"""


def search(node):

    pass


T = int(input())
for tc in range(1, T+1):
    V, E, sch1, sch2 = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = {}
    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]
        tree[parent] = tree.get(parent, []) + [child]
    print(tree)

    break