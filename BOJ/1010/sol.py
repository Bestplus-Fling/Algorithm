import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/1010
# 작성 코드 시작

memory = [1]
def cal_factorial(x):
    start = len(memory)
    for i in range(start, x + 1):
        memory.append(memory[i - 1] * i)

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    if len(memory) <= m:
        cal_factorial(m)
    print(memory[m] // (memory[n] * memory[m - n]))
