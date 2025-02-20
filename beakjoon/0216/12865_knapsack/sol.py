import sys
sys.stdin = open('input.txt', 'r')
#########################################

"""
부분집합으로 풀어보기
"""

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # N : 물건의 개수, K: 최대 하중
    N, K = map(int, input().split())
    _list = []
    for i in range(N):
        Weight, Value = map(int, input().split())
        _list.append((Value, Weight))
    # _list = [tuple(map(int, input().split())) for _ in range(N)]
    _list.sort(reverse=True)
    for i in range(N):
        d_W, d_V = _list[i]
        if d_W > N:
            continue
        W_list, V_list = [d_W], [d_V]
        for j in range(N):
            if j == i:
                continue
            W, V = _list[j]
            if sum(W_list) + W > K:
                continue
            W_list.append(W)
            V_list.append(V)
        if sum(W_list) <= K:
            max_value.append(sum(V_list))
    print(max(max_value))
