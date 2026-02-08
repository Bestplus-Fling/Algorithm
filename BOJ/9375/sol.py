import sys
from collections import defaultdict

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 9375
# 작성 코드 시작


def solve():
    n = int(input())
    if n == 0: return 0

    closet = defaultdict(int)
    for i in range(n):
        _, category = input().split()
        closet[category] += 1

    ans = 1
    for count in closet.values():
        ans *= (count + 1)

    return ans - 1


tc = int(input())
for t in range(tc):
    print(solve())