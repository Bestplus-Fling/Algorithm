import sys
sys.stdin = open('input.txt', 'r')
#########################################

def is_min(idx, num_sum, prev):
    global _min
    if num_sum >= _min:
        return
    if idx == N:
        _min = min(_min, num_sum)
        return
    for j in range(N):
        if j not in prev:
            prev.append(j)
            is_min(idx + 1, num_sum + matrix[idx][j], prev)
            prev.pop()


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    _min = float('inf')
    for i in range(N):
        is_min(1, matrix[0][i], [i])
    print(f'#{tc}',_min)

