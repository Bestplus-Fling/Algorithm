import sys
sys.stdin = open('input.txt', 'r')
#########################################


from collections import deque

# hex 생성할때마다 최대값 인덱스를 저장
def search_index(insert_num):
    # 최대값 위치 다음 인덱스에 저장, break
    idx = 0
    while True:
        # 배열에 값이 있고 배열의 길이가 K을 넘어가지 않을 때 내림차순으로 정렬
        if result and len(result) > idx:
            # result[idx] 값이 매개변수보다 작으면 idx위치에 insert
            if  int(result[idx], 16) < int(insert_num, 16):
                result.insert(idx, insert_num)
                break
            # result[idx]값이랑 동일하거나 idx가 len(result)-1일 경우 추가하지 않고 return한다.
            if int(result[idx], 16) == int(insert_num, 16):
                return
            idx += 1
        # 배열에 값이 없으면 추가만
        else:
            result.append(insert_num)
            return

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # N: 문자 길이, K: 내림차순했을 때 프린트하는 위치
    N, K = map(int, input().split())
    # 각 변(4)에 할당하는 문자열 길이
    hex_len = N // 4
    input_list = list(input())
    rotate = deque(input_list)
    result = []

    for i in range(hex_len):
        # 네 개의 슬라이싱을 만들어서 함수 호출하고, 호출한 함수에서 내림차순 정렬
        for j in range(0, N, hex_len):
            temp = list(rotate)[j:j + hex_len]
            search_index(''.join(temp))
        rotate.rotate(1)
    print(f'#{tc} {int(result[K-1], 16)}')


    #16진수 -> 10진수 변환
    # temp3 = int(temp2, 16)
    # print(temp3)

    # temp1 = list(rotate)[0:hex_len]
    # print(temp1)
    # temp2 = ''.join(temp1)
    # print(temp2)
