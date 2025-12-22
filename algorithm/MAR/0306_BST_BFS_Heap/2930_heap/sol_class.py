import sys
sys.stdin = open('input.txt', 'r')
#####################################
# from collections import deque
"""
연산1 - 숫자를 삽입
연산2 - 최대값 출력 후 해당 키값 삭제

구현 방법 - 현재 위치의 부모 노드 (idx // 2)와 대소비교(len > 1)
크다면 자리 교환 - idx // 2로 위치 갱신 후 대소비교
크지 않다면 종료 
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deq, ans_a = [0], []
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        # 반환 명령이 있을 때
        if arr[i][0] == 2:
            # 길이가 1, 트리에 아무것도 없으면 -1 추가
            if len(deq) == 1:
                ans_a.append(-1)
                break
            # 아니라면 root 를 출력 변수에 추가
            ans_a.append(deq[1])
            # 마지막 노드랑 root 랑 자리 교환
            deq[1] = deq[-1]
            # 마지막 노드(원래 root) 삭제
            deq.pop()
            # 삭제 후 root 의 max 를 보장
            # sort_tree(1)
            continue

        # 노드를 추가해야 한다면 일단 추가
        deq.append(arr[i][1])
        arr[i][1] = Node(arr[i][1])
        # 자식 노드가 있을 때 max root 확인
        if len(deq) > 2:
            pass
            # insert(len(deq) - 1)

    print(f'#{tc}', *ans_a)
# def sort_tree(root):
#     l, r = root * 2, (root * 2) + 1
#
#     # 조건 1. 자식 노드가 없으면 종료
#     if l >= len(deq) and r >= len(deq):
#         return
#
#     left = deq[l] if l < len(deq) else 0
#     right = deq[r] if r < len(deq) else 0
#
#     # 조건 2. 자식 노드가 있어도 자식들보다 현재 root 가 더 크면 종료
#     if deq[root] >= left and deq[root] >= right:
#         return
#
#     # 조건 3. 자식 노드보다 root 가 더 작다면 더 큰 쪽과 자리바꿈
#     if left >= right:
#         deq[root], deq[l] = deq[l], deq[root]
#         sort_tree(l)
#     else:
#         deq[root], deq[r] = deq[r], deq[root]
#         sort_tree(r)
#
#
# def insert(idx):
#     parent, child = idx // 2, idx
#     # 조건 1. root 이상(= 0)이 되면 종료
#     if parent == 0:
#         return
#     # 부모 노드보다 자식 노드가 더 크다면 자리 교환 후 재귀함수 호출
#     if deq[parent] < deq[child]:
#         # 자리 교환
#         deq[parent], deq[child] = deq[child], deq[parent]
#         insert(parent)
#     # 아니라면 종료
#     return
