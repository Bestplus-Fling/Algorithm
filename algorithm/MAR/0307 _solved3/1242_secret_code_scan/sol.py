import sys
sys.stdin = open('input.txt', 'r')
#####################################

# 비율을 저장하는 dict 생성
case = {
    (3, 2, 1, 1): 0, (1, 2, 3, 1): 5,
    (2, 2, 2, 1): 1, (1, 1, 1, 4): 6,
    (2, 1, 2, 2): 2, (1, 3, 1, 2): 7,
    (1, 4, 1, 1): 3, (1, 2, 1, 3): 8,
    (1, 1, 3, 2): 4, (3, 1, 1, 2): 9
}


def cut_code():
    for row in code:
        temp = ''
        # print(len(row))
        FLAG = False
        for i in range(M):
            # 문자열 형태로 입력받는 게 유리 temp += arr[i][j]
            if row[i] != '0':
                FLAG = True
            if FLAG:
                temp += row[i]
        t_list.append(temp)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    # 입력받은 배열을 순회 -> 0이 아닌 순간부터 0인 순간까지 확인
    t_list = []
    cut_code()
    bin_list = []
    ans = 0
    print(set(t_list))
    # 56의 배수가 될 때까지 temp = '0' + temp
    for cd in set(t_list):
        bin_num = list(bin(int(cd, 16))[2::])
        while True:
            if bin_num[-1] == '0':
                bin_num.pop()
            else:
                break
        bin_num = ''.join(bin_num)
        while len(bin_num) % 56 != 0:
            bin_num = '0' + bin_num
        # temp 길이 % 56의 몫을 저장
        bin_len = len(bin_num) // 56
        # bin_num의 시작값을 저장하는 변수를 생성
        case_list = []
        for i in range(0, 56 * bin_len, 7 * bin_len):
            slice_bin = ''
            for k in range(i, i+(7 * bin_len)):
                slice_bin += bin_num[k]
            check_bit = slice_bin[0]
            check = []
            count_case = 0
            for j in range(7 * bin_len):
                if check_bit == slice_bin[j]:
                    count_case += 1
                else:
                    check.append(count_case // bin_len)
                    check_bit = '1' if check_bit == '0' else '0'
                    count_case = 1
                if j == (bin_len * 7) - 1:
                    check.append(count_case // bin_len)
            # 값이 바뀌는 순간까지의 숫자를 비율로 저장= > tuple
            check = tuple(check[::])
            # 비율을 계산 -> dict에 등록된 숫자들로 가져오기
            case_list.append(case[check])
        print(case_list)
        # 8개의 숫자를 순회하면서 홀수, 짝수, 검증용으로 분해
        odd, even, flag = 0, 0, 0
        for i in range(8):
            if i % 2 == 0:
                odd += case_list[i]
            elif i != 7:
                even += case_list[i]
            else:
                flag = case_list[i]
        print((odd*3 + even + flag))
        if (odd*3 + even + flag) % 10 == 0:
            ans = max((odd + even + flag), ans)
        else:
            ans = 0
    print(f'#{tc}', ans)

