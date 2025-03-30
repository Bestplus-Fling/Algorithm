import sys
sys.stdin = open("16926.txt")
from collections import deque

N, M, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
x1, x2, y1, y2 = 0, N, 0, M
while x1 < x2 and y1 < y2:
    temp = deque()
    for i in range(x1, x2):
        if i == x1 or i == x2-1:
            for j in range(y1, y2):
                temp.append(grid[i][j])
        else:
            temp.extend([grid[i][y1], grid[i][y2-1]])
    k = ((x2-x1)*2) + ((y2-y1)*2) - 4
    k = R % k
    for _ in range(k):
        temp.append(temp.popleft())
    print(temp)
    x1, x2, y1, y2 = x1+1, x2-1, y1+1, y2-1
    