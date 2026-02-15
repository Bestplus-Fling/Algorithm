import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/9086
# 작성 코드 시작

t = int(input())
for tc in range(t):
    s = input().strip()
    print("".join([s[0], s[-1]]))