import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 1085
# 작성 코드 시작

x, y, w, h = map(int, input().split())
# 상하좌우의 이동거리 중 가장 짧은 것
a = min(abs(x - w), x)
b = min(y, abs(y - h))
print(min(a, b))