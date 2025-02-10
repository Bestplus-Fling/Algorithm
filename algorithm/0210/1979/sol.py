import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    check = 0
    for col in puzzle:
        cnt = 0
        if col.count(1) >= K:
            for i in range(N):
                if col[i] == 1:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == K and (i == N - 1 or (i+1 < N and col[i+1] == 0)):
                    check += 1
                    cnt = 0
                    continue

    for j in range(N):
        row = []
        for _ in range(N):
            row.append(puzzle[_][j])
        cnt = 0

        if row.count(1) >= K:
            for i in range(N):
                if row[i] == 1:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == K and (i == N - 1 or (i+1 < N and row[i+1] == 0)):
                    check += 1
                    cnt = 0
                    continue
    print(f'#{tc} {check}')
