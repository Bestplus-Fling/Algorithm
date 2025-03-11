import sys
sys.stdin = open('input.txt', 'r')
#####################################


# 깊이 우선 탐색(시작위치는 항상 0, 도착 위치는 항상 99)
def dfs(now_v=0):
    # 방문 처리
    visited[now_v] = True
    # 목표에 도달하면 1을 반환
    if now_v == 99:
        return 1
    # 현재 정점에 인접한 정점을 확인
    for adj_v in vertax[now_v]:
        if visited[adj_v]:
            continue
        if dfs(adj_v):
            return 1
    return 0


T = 10
for tc in range(1, T+1):
    t, N = map(int, input().split())
    _list = list(map(int, input().split()))
    visited = [False] * 100
    vertax = {}
    # 정점에서 뻗어나가는 간선이 없더라도 key value error 발생을 방지하기 위해
    # 일단 리스트형으로 만든다.
    for i in range(100):
        vertax[i] = []
    # 단방향 간선을 추가한다.
    for i in range(0, N*2, 2):
        vertax[_list[i]].append(_list[i+1])
    print(f'#{t}', dfs())