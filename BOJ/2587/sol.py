import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 2587
# 작성 코드 시작
n = 5
arr = [int(input()) for _ in range(n)]
print(sum(arr) // n)
print(sorted(arr)[2])