import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 10162
# 작성 코드 시작
timer = [300, 60, 10]

def solve():
    global timer
    counts = [0] * 3
    t = int(input())

    if t % 10 != 0:
        return [-1]

    for i in range(3):
        amount = t // timer[i]
        if amount > 0:
            t %= timer[i] * amount
            counts[i] = amount

    return counts

print(*solve())