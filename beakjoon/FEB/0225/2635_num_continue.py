N = int(input())

result_list = []
result_num = 0
for i in range(N-1, 0, -1):
    temp_list = [N, N-i, N - (N-i)]
    while temp_list[-1] > 0:
        temp_num = temp_list[-2] - temp_list[-1]
        if not (temp_num > 0):
            break
        temp_list.append(temp_num)
    count = len(temp_list)
    if count > result_num:
        result_list = temp_list
        result_num = count

print(result_num)
print(*result_list)
