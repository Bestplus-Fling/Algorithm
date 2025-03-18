for k in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    width = min(p1, p2) - max(x1, x2)
    height = min(q1, q2) - max(y1, y2)
    if width < 0 or height < 0:
        print('d')
    elif width == 0 and height == 0:
        print('c')
    elif width == 0 or height == 0:
        print('b')
    else:
        print('a')