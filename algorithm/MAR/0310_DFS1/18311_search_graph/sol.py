import sys
# from collections import defaultdict
sys.stdin = open('input.txt', 'r')
#####################################
# vertax = defaultdict(list)


# 깊이 우선 탐색
def dfs(now_v, temp=[]):
    # 현재 위치한 정점 번호를 추가
    temp.append(str(now_v))
    # 방문 처리
    visited[now_v] = True
    # 현재 정점에 인접한 정점들을 확인(정렬해서 작은 수를 우선 탐색)
    for arg_v in sorted(vertax[now_v]):
        # 방문된적 있는 정점은 건너뛴다.
        if visited[arg_v]:
            continue
        # 방문 된 적 없는 정점을 확인
        dfs(arg_v, temp)
    # 최종적으로 추가된 리스트를 반환
    return temp


# 입력
V, E = map(int, input().split())
edge = list(map(int, input().split()))
# 방문처리용 변수 선언
visited = [False] * (V + 1)
# 양방향으로 이동 가능하므로 인접한 정점의 정보를 dict 형태로 저장
vertax = {}
for i in range(0, len(edge), 2):
    start_v, end_v = edge[i], edge[i+1]
    vertax.setdefault(start_v, []).append(end_v)
    vertax.setdefault(end_v, []).append(start_v)
# 깊이 우선 탐색을 하면서 리스트에 저장, 저장된 리스트를 join할 때 '-'를 사이에 두고 합쳐서 출력
print("#1", '-'.join(dfs(1)))

