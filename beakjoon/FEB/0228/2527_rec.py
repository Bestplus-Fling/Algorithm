arr = [list(map(int, input().split())) for _ in range(4)]
for _list in arr:
    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = _list
    if bx1 < ax2 and by1 < ay2 or bx2 < ax1 and by2 < ay1:
        print('a')
    elif (bx1 == ax2 or by1 == ay2) or (bx2 == ax1 or by2 == ay1):
        print('b')
    elif (bx1 == ax2 and by1 == ay2) or (bx2 == ax1 and by2 == ay1):
        print('c')
    else:
        print('d')