import sys
sys.stdin = open('input.txt', 'r')
#####################################

"""
암호코드는 8개의 숫자로 이루어져있다.
암호코드에서 숫자 하나는 7개의 비트로 암호화 되어 주어진다. (=암호코드의 가로 길이는 56)
올바른 암호코드 = (홀수 자리의 합 * 3) + (짝수 자리의 합)이 10의 배수

"""

T = int(input()) # test case개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    # print(matrix)
    for i in range(N):
        if matrix[i].count('1') > 0:
            check = [matrix[i][_] for _ in range(M)]
            break

    check.reverse()
    idx = check.index("1")
    bin_list, temp = [], []
    for i in range(idx, idx+57):
        temp.append(check[i])
        if len(temp) == 7:
            bin_list.append(list(reversed(temp)))
            temp = []
    print(len(bin_list))

    num_list = []
    for i in range(8):
        print(bin_list[i])
        num = int(''.join(bin_list[i]), 2)
        num_list.append(num)
    print(num_list)
    break