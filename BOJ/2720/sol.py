import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 2720
# 작성 코드 시작

coins = [25, 10, 5, 1]

t = int(input())
for tc in range(t):
    counts = [0] * 4
    c = int(input())

    for i in range(4):
        num = c // coins[i]
        if num > 0:
            counts[i] += num
            c -= coins[i] * num
    print(*counts)

