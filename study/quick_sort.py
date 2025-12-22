list1 = [7, 35, 23, 8, 4, 3, 2, 9]


def quick_sort(num_list):
    # 리스트의 길이가 1 이하면 그대로 반환한다
    if len(num_list) <= 1:
        return num_list
    #pivot을 설정하고 pivot을 기준으로 작은 값과 큰 값을 저장하는 리스트를 생성한다
    left_list, right_list = [], []
    pivot = num_list[0]
    # num_list를 순회하면서 pivot을 기준으로 작은 값은 left에 큰 값은 right에 저장
    for i in range(1, len(num_list)):
        if num_list[i] <= pivot:
            left_list.append(num_list[i])
        else:
            right_list.append(num_list[i])
    print(left_list, right_list)


print(quick_sort(list1))