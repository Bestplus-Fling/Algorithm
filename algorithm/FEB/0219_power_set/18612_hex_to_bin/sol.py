import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = input().strip()
    arr = []

    # for문으로 hex -> decimal 변경
    for num in N:
        # 16진수를 10진수로 변경
        tmp = int(num, 16)
        # tmp 를 2진수로 변경
        _list = []
        for i in range(4):
            if num and tmp != 0:
                _list.append(tmp % 2)
                tmp = tmp // 2
        # 한 자리 16진수를 표현하기 위한 2진수의 자리는 4개가 필요하므로 부족한 자리는 0으로 채운다.
        while len(_list) != 4:
            _list.append(0)
        # 최종적으로 사용할 2진수를 저장한다.
        arr.append(list(reversed(_list)))
    # 2진수를 7자리씩 끊어낸다.
    out_list, temp = [], []
    for _hex in arr:
        for j in _hex:
            temp.append(int(j))
            if len(temp) == 7:
                out_list.append(temp)
                temp = []
    if temp:
        out_list.append(temp)
    # 최종 출력 형태로 변환
    result = []
    for i in out_list:
        tem = 0
        for j in range(len(i)):
            tem += (2 ** j) * i[-(j+1)]
        result.append(tem)

    print(f'#{tc}', *result)





