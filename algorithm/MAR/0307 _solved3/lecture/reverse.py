a = 123456789
b = []
while a != 0:
    b.append(str(a % 10))
    a = a // 10
print(''.join(b))