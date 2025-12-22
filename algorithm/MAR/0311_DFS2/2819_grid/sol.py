import sys
sys.stdin = open('input.txt', 'r')
#####################################

# 델타
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


# 문자열로 관리, cnt로 길이 확인
def dfs(x, y, cnt, st=''):
    st += str(arr[x][y])
    # 처음 시작은 0부터 하기 때문에, 6이 된 순간은 문자열의 길이가 7일 때
    if cnt == 6:
        res.append(st)
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < 4 and 0 <= ny < 4):
            continue
        dfs(nx, ny, cnt+1, st)


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    res = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0)
    # 중복 제거
    result = set(res[::])
    print(f'#{tc}', len(result))
