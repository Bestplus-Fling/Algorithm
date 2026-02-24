import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/2775
# 작성 코드 시작
def solve():
    k = int(input())
    n = int(input())
    arr = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        arr[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    return arr[k][n]


t = int(input())
for t in range(t):
    print(solve())