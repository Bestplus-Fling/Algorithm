import sys
sys.stdin = open('1068.txt', 'r')
from collections import deque


def bfs(root):
    queue = deque([root])
    cnt = 0
    while queue:
        parent = queue.popleft()
        if not tree[parent]:
            cnt += 1
            continue
        for child in tree[parent]:
            queue.append(child)
    return cnt


N = int(input())
tree = [[] for _ in range(N)]
temp = list(map(int, input().split()))
delete = int(input())

for idx, status in enumerate(temp):
    # root 노드를 저장
    if status == -1:
        rt = idx
        continue
    # 삭제하려는 노드를 만나면 continue
    if status == delete or idx == delete:
        continue
    tree[status].append(idx)
print(bfs(rt) if rt != delete else 0)
