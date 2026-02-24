import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 32978
# 작성 코드 시작

n = int(input())
s = set(list(input().split()))
for ingredient in list(input().split()):
    s.remove(ingredient)
print(*list(s))