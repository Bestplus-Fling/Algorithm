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
        FLAG = False
        ct = 0
        for wd in row:
            # 문자열 형태로 입력받는 게 유리 temp += arr[i][j]
            if wd != '0':
                FLAG = True
            if FLAG:
                temp += wd
                if wd == '0':
                    ct += 1
                else:
                    ct = 0
                if ct == 2:
                    FLAG = False
                    t_list.append(temp)
                    temp = ''
                    ct = 0
        if temp:
            t_list.append(temp)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    # 16진수의 숫자만을 저장한 후 중복 제거
    t_list = []
    cut_code()
    print(set(t_list))
    # 2진수로 변환된 자료형을 저장할 변수 선언
    bin_list = []
    ans = 0

    # for loop 동작
    """
    1. 뒤에 붙은 0을 제거한다.
    2. 2진수의 길이를 56의 배수에 맞추기 위해 0을 앞쪽에 추가한다.
    3. 56의 배수를 저장한다.
    4. 7자리씩 잘라서 확인
    """
    for cd in set(t_list):

        # 1번: 뒤에 붙은 0을 제거

        bin_num = list(bin(int(cd, 16))[2::])
        if len(bin_num) < 30:
            continue
        # 1차적으로는 끝에 붙은 영을 제거한다.
        while True:
            if bin_num[-1] == '0':
                bin_num.pop()
            else:
                break

        # 2번: 2진수 길이를 56의 배수로 맞춘다.
        bin_num = ''.join(bin_num)

        while len(bin_num) % 56 != 0:
            bin_num = '0' + bin_num
        print(bin_num, '\n', len(bin_num))
        # 3번: 56의 몇배수인지 확인한다.
        bin_len = len(bin_num) // 56

        # 4. 7자리씩 잘라서 확인한다.
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
            FLAG = False
            for _ in check:
                if _ > 4 or _ <= 0:
                    FLAG = True
                    break
            if FLAG or len(check) != 4:
                break
            # 값이 바뀌는 순간까지의 숫자를 비율로 저장= > tuple
            check = tuple(check[::])
            # print(check)
            # 비율을 계산 -> dict에 등록된 숫자들로 가져오기
            case_list.append(case[check])
        if not case_list:
            break
        print(case_list)
        # 8개의 숫자를 순회하면서 홀수, 짝수, 검증용으로 분해
        odd, even, flag = 0, 0, 0
        for i in range(8):
            if i % 2 == 0:
                odd += case_list[i]
            elif i == 7:
                flag += case_list[i]
            else:
                even += case_list[i]
        print((odd*3 + even + flag))
        if (odd*3 + even + flag) % 10 == 0:
            ans += (odd + even + flag)
    print(f'#{tc}', ans)

