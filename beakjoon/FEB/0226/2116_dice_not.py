# 마주보는 주사위끼리 확인하기 위한 리스트
check_list = [5, 3, 4, 1, 2, 0]
# 주사위 개수 N
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째 주사위에서 1이 있는 인덱스를 찾는다.
idx = arr[0].index(1)
# 1과 마주보는 숫자를 저장한다
next_num = arr[0][check_list[idx]]
result = []
for i in range(N):
    # next_num 과 일치하는 숫자의 인덱스를 확인
    idx = arr[i].index(next_num)
    # print(idx, check_list[idx])
    # 마주보는 숫자를 next_num 에 저장
    next_num = arr[i][check_list[idx]]
    max_temp = 0
    for j in range(6):
        if j == idx or j == check_list[idx]:
            continue
        max_temp = max(arr[i][j], max_temp)
    result.append(max_temp)
print(sum(result))





