import sys
sys.stdin = open("2427.txt")


for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    line1 = [i for i in range(x1, p1+1)]
    line2 = [i for i in range(y1, q1+1)]
    line3 = [i for i in range(x2, p2+1)]
    line4 = [i for i in range(y2, q2+1)]
    row, col = 0, 0
    for num in line1:
        row += 1 if line3.count(num) else 0
    for num in line2:
        col += 1 if line4.count(num) else 0

    if not col or not row:
        print('d')
    elif row == 1 and col == 1:
        print('c')
    elif row == 1 or col == 1:
        print('b')
    else:
        print('a')


    # if (x2 != p1 and y2 != q1) or (x1 != p2 and y1 != q2):
    #     print('d')
    # elif (x2 == p1 and y2 == q1) or (x1 == p2 and y1 == q2):
    #     print('c')
    # elif (x2 == p1 or y2 == q1) or (y1 == q2 or x1 == p2):
    #     print('b')
    # else:
    #     print('a')
    # x = p1+1 if p1 > p2 else p2+1
    # y = q1+1 if q1 > q2 else q2+1
    # matrix = [[0] * x for _ in range(y)]
    #
    # for i in range(y1, q1+1):
    #     for j in range(x1, p1+1):
    #         matrix[i][j] += 1
    # for i in range(y2, q2+1):
    #     for j in range(x2, p2+1):
    #         matrix[i][j] += 1
    #
    # row, col = 0, 0
    # for i in range(y):
    #     temp = matrix[i].count(2)
    #     if temp:
    #         row += 1
    #         col += temp
    # if not row and not col:
    #     print('d')
    # elif row == 1 and col == 1:
    #     print('c')
    # elif row == 1 and col > 1:
    #     print('b')
    # else:
    #     print('a')





