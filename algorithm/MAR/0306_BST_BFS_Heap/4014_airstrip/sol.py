import sys
sys.stdin = open('input.txt', 'r')
#####################################


def check(arr, i, j, dir):
    # 현재 위치부터 x칸만큼의 활주로 건설 가능 여부를 반환
    for k in range(X):
        x = j + (k * dir)
        # 건설 중 범위를 벗어나거나, 지형의 변화가 있거나, 이미 활주로가 있다면
        if not(0 <= x < N) or arr[j] != arr[x] or slope[i][x]:
            # 설치 불가능
            return True
        # 활주로 설치여부 확인
        slope[i][x] = True
    # for 문 정상 종료시 설치 가능
    return False



def search(grid):
    # 건설 가능한 활주로의 개수를 확인
    count = 0
    for i in range(N):
        for j in range(N-1):
            # 지형의 높이가 2 이상 넘어가면 탐색 x
            if abs(grid[i][j] - grid[i][j + 1]) >= 2:
                break
            # 현재 위치보다 다음 칸의 값이 크다면, 현재 위치를 포함
            # x 칸만큼 길이의 경사로를 설치할 수 있는지 확인
            if grid[i][j] < grid[i][j+1]:
                if check(grid[i], i, j, -1):
                    break
            # 현재 위치보다 다음 칸의 값이 작다면, 다음 위치부터
            # x 칸만큼 길이의 경사로를 설치할 수 있는지 확인
            if grid[i][j] > grid[i][j+1]:
                if check(grid[i], i, j+1, 1):
                    break
        # 정상종료했다? -> 활주로 사용 가능!!
        else:
            count += 1
    return count


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 정방행렬에 대한 탐색
    """
    단차가 발생했을 때 발생한 시점에서 x칸 이내 변경점이 있다면 활주로 x
    범위 밖을 벗어나면 그때도 불가
    """

    ans = 0
    slope = [[False] * N for _ in range(N)]
    ans += search(matrix)

    matrix_rotation = list(zip(*matrix[::-1]))
    slope = [[False] * N for _ in range(N)]
    ans += search(matrix_rotation)
    print(f'#{tc}', ans)


