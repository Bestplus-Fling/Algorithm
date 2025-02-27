"""
N 개의 글자가 주어질 때
행*열 = N이어야 하며 이때 열이 행보다 크거나 같아야 한다(R*C=N, R<=C)
이 경우를 만족하는 경우가 많을 경우 R이 큰 경우를 선택한다.
"""

text = input()
N = len(text)
RC = (0, 0)
for R in range(1, N+1):
    if N % R != 0:
        continue
    C = N//R
    if R <= C:
        RC = (R, C)
    else:
        break
row, col = RC
arr = [[''] * row for _ in range(col)]
idx = 0
for i in range(col):
    for j in range(row):
        arr[i][j] = text[idx]
        idx += 1
arr = list(zip(*arr))
for i in range(row):
    for j in range(col):
        print(arr[i][j], end='')


