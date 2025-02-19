import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = input().strip()
    arr = []
    for num in N:
        # 16진수를 10진수로 변경
        tmp = int(num, 16)
        # 16진수를 10진수화 한 걸 2진수로 변경(4자리 고정)
        _list = []
        for i in range(4):
            if num and tmp != 0:
                _list.append(tmp % 2)
                tmp = tmp // 2
        while len(_list) != 4:
            _list.append(0)
        arr.append(list(reversed(_list)))
    # print(arr)
    out_list, temp = [], []
    for _hex in arr:
        for j in _hex:
            temp.append(j)
            if len(temp) == 7:
                out_list.append(temp)
                temp = []
    if temp:
        out_list.append(temp)
    # print(out_list)
    result = []
    for i in out_list:
        tem = 0
        for j in range(len(i)):
            tem += (2 ** j) * i[-(j+1)]
        result.append(tem)

    print(f'#{tc}', *result)





