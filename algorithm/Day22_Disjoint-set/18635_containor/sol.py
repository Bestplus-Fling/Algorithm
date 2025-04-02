import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    is_move = [False] * N
    ans = 0
    for i in range(M):
        # 트럭이 옮길 수 있는 무게 truck[i]와 중량
        for j in range(N):
            if is_move[j]: continue
            # 옮긴 적 없는 화물 중 무게가 나보다 무거우면 continue
            if truck[i] < weight[j]: continue
            # 나보다 가벼우면 무조건 이동
            ans += weight[j]
            is_move[j] = True
            break
    print(f'#{tc}', ans)
