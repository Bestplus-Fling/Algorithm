arr = [int(input()) for _ in range(10)]

temp = [-1]
result = 0
for idx in arr:
    temp_else = idx % 42
    if temp.count(temp_else) == 0:
        result += 1
    temp.append(temp_else)
print(result)