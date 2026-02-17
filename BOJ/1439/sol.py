import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/1439
# 작성 코드 시작

s = input().strip()
count = [0] * 2
count[int(s[0])] = 1
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        count[int(s[i])] += 1
print(min(count))