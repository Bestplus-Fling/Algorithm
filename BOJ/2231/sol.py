import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 2231
# 작성 코드 시작

def solve():
    n_str = input().strip()
    n = int(n_str)
    start = max(1, n - len(n_str) * 9)

    for i in range(start, n):
        temp = i
        digit_sum = i
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        if digit_sum == n:
            return i
    return 0

print(solve())
# for i in range(n - 1, 0, -1):
#     x = i + sum(map(int, str(i)[::]))
#     if x == n and ans > i:
#         ans = i
# print(ans)
