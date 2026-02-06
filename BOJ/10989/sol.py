import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 10989
# 작성 코드 시작
MAX_NUM = 10001
n = int(input())
counting_arr = [0] * MAX_NUM
for _ in range(n):
    x = int(input())
    counting_arr[x] += 1
for i in range(1, MAX_NUM):
    while counting_arr[i]:
        print(i)
        counting_arr[i] -= 1
