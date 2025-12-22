import sys
sys.stdin = open('input.txt', 'r')
#########################################
'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

입력
첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
1<=T<=10, 10<=N<=1000

출력
#과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
'''
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    #입력 : N(숫자열의 길이), num(숫자열)
    N = int(input())
    num = input()
    # 1의 길이를 확인 / 가장 긴 1의 연속한 수를 저장
    check_one, max_num = 0, 0
    for i in range(N):
        if int(num[i]) == 1:
            check_one += 1
            # 최대값 갱신
            if max_num < check_one:
                max_num = check_one
        # 0을 만나면 연속한 1의 수 확인을 초기화
        else:
            check_one = 0
    print(f'#{tc} {max_num}')

