"""
붙여진 색종이의 둘레를 구한다.
어떻게?

방법 1 : 둘레의 숫자를 2, 사각형 내부를 1로 생각한다.
    행 열의 특정 숫자(시작, 끝)일 경우 2를, 아닐 경우 1을 대입한다
    숫자 1(사각형 내부)은 그냥 칠한다.
    숫자 2(테두리)는 해당 위치에 숫자가 없을 때 칠한다.
방법 2 :
"""
N = int(input())
outside = 0
matrix = [[0] * 100 for _ in range(100)]
for idx in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            # 현재 위치에 숫자가 테두리로 입력되어 있는데
            check = i == y or i == y + 9 or j == x or j == x + 9
            if matrix[i][j] == 2:
                # 테두리를 칠할 때가 아니면 1을 입력
                if not check:
                    matrix[i][j] = 1
                    outside -= 1
                    continue
            if not matrix[i][j]:
                if check:
                    matrix[i][j] = 2
                    outside += 1
                else:
                    matrix[i][j] = 1

dxy = [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]

for i in range(100):
    for j in range(100):
        if matrix[i][j] != 2:
            continue
        val_TF = False
        count = 0
        for dx, dy in dxy:
            ni, nj = i + dx, j + dy
            if not matrix[ni][nj]:
                continue
            count += 1
        if count == 8:
            outside -= 1
            matrix[i][j] = 1
print(outside)


# for i in range(100):
#     print(matrix[i])
#     # outside += matrix[i].count(2)

from itertools import permutations