import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 14888
# 작성 코드 시작
calculator = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: int(x / y)
]

def dfs(index, value):
    global min_val, max_val, operator
    if index == n:  # 종료조건: 연산자 모두 소진
        min_val = min(min_val, value)
        max_val = max(max_val, value)

    for i in range(4):
        if not operator[i]: continue
        operator[i] -= 1
        dfs(index + 1, calculator[i](value, arr[index]))
        operator[i] += 1
    pass

n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_val, max_val = float("inf"), float("-inf")
dfs(1, arr[0])
print(max_val, min_val, sep="\n")
