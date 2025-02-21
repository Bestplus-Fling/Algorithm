N = int(input())

max_list = []
for i in range(1, N+1):
    temp = [N, i]
    idx = 0
    while True:
        num = temp[idx] - temp[idx + 1]
        if num < 0:
            break
        temp.append(num)
        idx += 1
    if len(max_list) < len(temp):
        max_list = temp
print(len(max_list))
print(*max_list)