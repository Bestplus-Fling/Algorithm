import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 25325
# 작성 코드 시작
n = int(input())

st = {name: 0 for name in list(input().split())}

for _ in range(n):
    for name in list(input().split()):
        st[name] += 1

for k, v in sorted(st.items(), key=lambda x: (-x[1], x[0])):
    print(k, v)