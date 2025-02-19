import sys
sys.stdin = open('input.txt', 'r')
#########################################

from pprint import pprint

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    mat, temp = [], []
    for i in range(N):
        for j in range(10):
            temp.append(arr[i][j])
            if len(temp) == 7:
                mat.append(temp)
                temp = []
    # pprint(mat)
    result = []
    for _list in mat:
        temp = 0
        for j in range(7):
            temp += (2 ** j) * _list[-(j+1)]
        result.append(temp)
    # print()
    print(f"#{tc}", *result)
