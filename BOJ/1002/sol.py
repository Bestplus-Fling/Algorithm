import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/1002
# 작성 코드 시작

def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

    sum_r_sq = (r1 + r2) ** 2
    diff_r_sq = (r1 - r2) ** 2

    if d_sq == 0 and r1 == r2:
        return -1

    # 한 점에서 외접 혹은 내접하는 경우
    if d_sq == sum_r_sq or d_sq == diff_r_sq:
        return 1

    if diff_r_sq < d_sq < sum_r_sq:
        return 2

    return 0

t = int(input())
for tc in range(t):
    print(solve())
