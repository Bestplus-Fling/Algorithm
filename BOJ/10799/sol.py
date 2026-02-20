import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/10799
# 작성 코드 시작

s = input().strip()
pipe = ans = i = 0

while i <= len(s) - 1:
    if s[i] == '(':
        if s[i + 1] == ')':
            ans += pipe
            i += 1
        else:
            pipe += 1
    else:
        pipe -= 1
        ans += 1
    i += 1
print(ans + pipe)