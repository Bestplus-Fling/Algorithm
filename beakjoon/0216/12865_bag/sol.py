import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    _list = [tuple(map(int, input().split())) for _ in range(N)]
    max_value = []
    for i in range(N):
        d_W, d_V = _list[i]
        W_list, V_list = [d_W], [d_V]
        for j in range(N):
            if j == i:
                continue
            W, V = _list[j]
            if sum(W_list) + W > K:
                continue
            W_list.append(W)
            V_list.append(V)
        max_value.append(sum(V_list))
    print(max(max_value))
