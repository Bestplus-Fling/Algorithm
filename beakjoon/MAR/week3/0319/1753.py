import sys
sys.stdin = open('1753.txt', 'r')
#########################################
from collections import defaultdict


def run(vtx, endv, depth=0, weight=0):
    # 정점을 순회하면서 반환받은 값의 최소값만을 저장한다.
    # 그리고 순회가 끝나면 그 최소값을 다시 반환한다.
    # 만약 최소값이 float('inf')라면, return은 'INF'를 한다
    limit = float('inf')
    if vtx == endv:
        return depth, weight

    for adj in graph[vtx]:


    pass


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
point = defaultdict(int)
# 둘째 줄에는 시작 정점의 번호 K가 주어진다.
stv = int(input())
# 셋째 줄부터 E 개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수(u, v, w)가 순서대로 주어진다
# u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻
# u와 v는 서로 다르며 w는 10 이하의 자연수
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append(v)
    point[(u, v)] = w
print(graph)
print(point)

for v in range(1, V+1):
    if v == stv:
        print(0)
        continue
    # 방문처리 변수 생성
    vit = [0] * (V+1)
    print(run(stv, v))
