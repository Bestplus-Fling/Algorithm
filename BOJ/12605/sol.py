import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/12605
# 작성 코드 시작
tc = int(input())
for t in range(1, tc + 1):
    arr = list(input().split())
    print(f"Case #{t}:", *reversed(arr))