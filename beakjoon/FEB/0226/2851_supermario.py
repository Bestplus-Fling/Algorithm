temp = 0
for i in range(10):
    N = int(input())
    if temp + N >= 100:
        break
    temp += N

a = 100 - temp
c = temp + N - 100
print(temp+N if a == c or a > c else temp)

