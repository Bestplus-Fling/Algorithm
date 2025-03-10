import sys
sys.stdin = open('input.txt', 'r')
#####################################


# 깊이 우선 탐색
def dfs(now_v):
    # 방문 처리
    visited[now_v] = True
    # 목표한 정점에 도달하면 1을 반환
    if now_v == G:
        return 1
    # 현재 정점에 인접한 정점을 순회
    for arg_v in vertax[now_v]:
        # 방문 된 적 있다면 건너뛴다.
        if visited[arg_v]:
            continue
        # 정점을 찾은 경우라면 1을 반환
        if dfs(arg_v):
            return 1
    # 모든 정점을 확인했으나 G를 찾지 못하면 0을 반환
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    vertax = {}
    for i in range(1, V+1):
        vertax[i] = []
    # 단방향 간선을 dict 형태로 저장
    for _ in range(E):
        start_v, end_v = map(int, input().split())
        vertax[start_v].append(end_v)
    S, G = map(int, input().split())
    # 방문 처리용 변수
    visited = [False] * (V+1)
    # 시작 위치에서 G까지 도달할 수 있는지 확인
    print(f'#{tc}', dfs(S))
