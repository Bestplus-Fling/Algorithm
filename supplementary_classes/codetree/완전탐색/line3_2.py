n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

lines = []


# F(i): i-1번째까지는 가로/세로가 정해졌고,
#       i번째에 가로세로를 정해서 i+1번째의 선택을 시키게 하는 함수
def F(i):
    global lines
    # 탈출(정해야하는 point는 0~n-1이므로 i >= n이 되면 탈출)
    if i >= n:
        # 정해진 가로/세로에 대해 중복 없이 3개인지 확인
        return len(set(lines)) == 3

    # 본문 (i번째 점을 지나는 선이 가로/세로 인지 선택하고 i+1번째로 넘기기)
    # 가로
    lines.append(('y', points[i][1]))
    if F(i + 1):
        return True
    lines.pop()

    # 세로
    lines.append(('x', points[i][0]))
    if F(i + 1):
        return True
    lines.pop()

    return False


# 각 점에 대해 가로/세로를 정한다
# 정해진 가로세로에 대해 중복없이 3개인지 확인

print(int(F(0)))