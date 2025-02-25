"""
input
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
"""
matrix = [[0] * 100 for _ in range(100)]
count = 0
for four in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if matrix[i][j]:
                continue
            matrix[i][j] += 1
            count += 1

print(count)



