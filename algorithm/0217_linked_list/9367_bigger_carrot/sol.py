import sys
sys.stdin = open('input.txt', 'r')
#########################################


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 당근의 개수를 입력
    N = int(input())
    # 당근의 크기를 리스트 형태로 입력받는다.
    C_list = list(map(int, input().split()))
    # 크기가 커지는 과정을 계수해서 저장
    max_cnt = []
    for i in range(N):
        # 연속으로 커지지 않는 경우 구간의 최소 길이 1을 보장
        cnt = 1
        for j in range(i, N-1):
            # 만약 현재 요소보다 다음에 오는 요소가 크다면
            # => 연속으로 커지는 경우라면 계수
            if C_list[j] < C_list[j + 1]:
                cnt += 1
            # 아닐 경우 탐색을 멈춘다.
            else:
                break
        # 증가하다가 감소했을때 까지 계수를 리스트에 저장
        max_cnt.append(cnt)
    # 가장 많이 증가했던 경우를 출력
    print(f'#{tc} {max(max_cnt)}')
