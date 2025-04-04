import sys
sys.stdin = open('input.txt', 'r')
#########################################


"""
순열 후 반으로 나눴을 때 run, triplet 구분해서 확인"""

# def permutation():
#     pass


# import itertools

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    arr = list(map(int, input().strip()))
    arr_dict = {}
    for i in arr:
        arr_dict[i] = arr_dict.get(i, 0) + 1
    for i in arr:
        if arr_dict[i] >= 3:
            temp = (arr_dict[i] // 3) * 3
            for j in range(temp):
                arr_dict[i] -= 1
        if arr_dict[i] != 0:
            count = 0
            _list = [i]
            for j in range(1, 3):
                if i+j in arr_dict.keys() and arr_dict[i+j] > 0:
                    _list.append(i+j)
                    count += 1
                else:
                    break
            if count != 2:
                continue
            # print(_list)
            for j in _list:
                arr_dict[j] = arr_dict.get(j) - 1
    # print(arr_dict)
    print(f'#{tc}', 'true' if max(arr_dict.values()) == 0 and min(arr_dict.values()) >= 0 else 'false')



    # # print(arr)
    # ll = list(itertools.permutations(sorted(arr), 3))
    # # print(ll)
    # for tp in ll:
    #     count = 0
    #     for 5256_binomial coefficient in range(1, 3):
    #         if tp[-5256_binomial coefficient] - tp[-(5256_binomial coefficient+1)] == 1:
    #             count += 1
    #     if count == 2:
    #         for j in tp:
    #             if j in arr:
    #                 arr.remove(j)
    # print(arr)
    # _list = list(itertools.permutations(arr))
    # for tp in _list:
