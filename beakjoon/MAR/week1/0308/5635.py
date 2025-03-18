_list = sorted([input().split() for _ in range(int(input()))], key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
print(_list[0][0])
print(_list[-1][0])


