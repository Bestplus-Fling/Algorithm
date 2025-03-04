import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    check = 0
    for i in range(N):
        cnt_row = cnt_col = 0
        row_list = puzzle[i][::]
        if puzzle[i][::].count(1) >= K:
            for j in range(N):
                if row_list[j] == 1:
                    cnt_row += 1
                else:
                    cnt_row = 0
                    continue
                if cnt_row == K and (j == N - 1 or (j+1 < N and row_list[j+1] == 0)):
                    check += 1
                    cnt_row = 0

        for j in range(N):
            if puzzle[j][i] == 1:
                cnt_col += 1
            else:
                cnt_col = 0
                continue
            if cnt_col == K and (j == N - 1 or (j+1 < N and puzzle[j+1][i] == 0)):
                check += 1
                cnt_col = 0
    print(f'#{tc} {check}')
