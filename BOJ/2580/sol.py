import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 2580
# 작성 코드 시작
size = 9
gen_check_arr = lambda: [[False] * 10 for _ in range(size)]
row_used = gen_check_arr()
col_used = gen_check_arr()
box_used = gen_check_arr()

cal_coord_index = lambda r, c: (r // 3) * 3 + (c // 3)

def change_stat(r, c, n, status):
    row_used[r][n] = status
    col_used[c][n] = status
    box_used[cal_coord_index(r, c)][n] = status

def dfs(idx):
    if idx == len(coord):
        return True

    r, c = coord[idx]
    box_idx = cal_coord_index(r, c)
    for n in range(1, 10):
        # if row_used[r][n] or col_used[c][n] or box_used[cal_coord_index(r, c)][n]:
        if row_used[r][c] or col_used[c][n] or box_used[box_idx][n]:
            continue
        change_stat(r, c, n, True)
        matrix[r][c] = n
        if dfs(idx + 1):
            return True
        change_stat(r, c, n, False)
        matrix[r][c] = 0
    return False

matrix = [list(map(int, input().split())) for _ in range(size)]
# 좌표 기록
coord = []
for i in range(size):
    for j in range(size):
        if matrix[i][j] == 0:
            coord.append((i, j))
        else:
            change_stat(i, j, matrix[i][j], True)
dfs(0)
for i in range(size):
    print(*matrix[i])
