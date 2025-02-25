# 부등호 방향 잘 생각하기
# 조건 확인 잘 하기

N = int(input())

result_num = 0
for i in range(1, N+1):
    temp_list = [N, i]
    while True:
        num = temp_list[-2] - temp_list[-1]
        if num < 0:
            break
        temp_list.append(num)
    count = len(temp_list)
    if count > result_num:
        result_list = temp_list
        result_num = count

print(result_num)
print(*result_list)
