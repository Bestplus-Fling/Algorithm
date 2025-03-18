import sys
sys.stdin = open('input3.txt', 'r')
#####################################


def sort_tree(root):
    l, r = root * 2, (root * 2) + 1
    largest = root

    if l < len(deq) and deq[l] > deq[largest]:
        largest = l
    if r < len(deq) and deq[r] > deq[largest]:
        largest = r
    if largest != root:
        sort_tree(largest)


def insert(idx):
    parent, child = idx // 2, idx
    # 조건 1. root 이상(= 0)이 되면 종료
    if parent == 0:
        return
    # 부모 노드보다 자식 노드가 더 크다면 자리 교환 후 재귀함수 호출
    if deq[parent] < deq[child]:
        # 자리 교환
        deq[parent], deq[child] = deq[child], deq[parent]
        insert(parent)
    # 아니라면 종료
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    inputs = [tuple(map(int, input().split())) for _ in range(N)]
    deq, ans_a = [0], []
    for i in range(N):
        arr = inputs[i]
        if arr[0] == 2:         # 반환 명령이 있을 때
            if len(deq) == 1:   # 길이가 1, 트리에 아무것도 없으면 -1 추가
                ans_a.append(-1)
                continue
            ans_a.append(deq[1])  # 아니라면 root 를 출력 변수에 추가
            deq[1] = deq[-1]    # 마지막 노드랑 root 랑 자리 교환
            deq.pop()           # 마지막 노드(원래 root) 삭제
            sort_tree(1)        # 삭제 후 root 의 max 를 보장
            continue
        # 노드를 추가해야 한다면 일단 추가
        deq.append(arr[1])
        # 자식 노드가 있을 때 max root 확인
        if len(deq) > 2:
            insert(len(deq) - 1)

    print(f'#{tc}', *ans_a)
