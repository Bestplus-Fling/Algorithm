import sys
# sys.stdin = open('input/2644_1.txt', 'r')
sys.stdin = open('input/2644_2.txt', 'r')
#########################################


def search(now, depth=0):
    if now == E:
        return depth
    # 자기 자식중에 확인
    # 없으면 부모로 이동
    visited[now] = 1
    print(f"현재 {now}, 촌수는 {depth}")
    # 자기 자식 중에 E가 있는 지 확인
    for child in children[now]:
        if child == E:  # 있다면 이동하지 않은 촌수까지 돌려준다.
            return depth+1
        if visited[child]:
            continue
        # 없다면 다른 자식들을 방문
        print(f"{child}로 이동")
        temp = search(child, depth+1)
        if temp != 0:
            return temp
    # 자식들 다 돌아봤는데도 없다면, 부모로 이동
    if not visited[parent[now]]:
        return search(parent[now], depth + 1)
    # 부모도 방문한 적 있다면 그냥 돌아간다.
    return 0


N = int(input())
S, E = map(int, input().split())
parent = [0] * (N + 1)
children = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(int(input())):
    x, y = map(int, input().split())
    children[x].append(y)
    parent[y] = x
# print(children, who_parent, sep='\n')
result = search(S)
print(result if result != 0 else -1)
