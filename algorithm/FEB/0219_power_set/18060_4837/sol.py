import sys
sys.stdin = open('input.txt', 'r')
#########################################

"""
1부터 12까지의 숫자를 원소로 가진 집합 A
부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력
ex) N이 3, K가 6일 경우 부분집합은 1, 2, 3이다.
"""


def power_set(idx, num_sum, cnt):
    global count
    # 종료조건 : num_sum의 배열 길이가 N이고 sum(num_sum)이 K와 같다면
    if cnt == N:
        count += 1 if num_sum == K else 0
        return
    # 종료2: idx가 len(arr)과 같아지는 경우
    if idx == len(arr):
        return

    # 현재 idx를 포함(선택)한 경우
    power_set(idx + 1, num_sum + arr[idx], cnt + 1)
    # 현재 arr[idx]를 포함하지 않는 경우
    power_set(idx + 1, num_sum, cnt)


arr = [i for i in range(1, 13)]
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    power_set(0, 0, 0)
    print(f'#{tc} {count}')



