a = 123456789
c = []
while a != 0:
    c.append(str(a % 10))
    a = a // 10
print(''.join(c))