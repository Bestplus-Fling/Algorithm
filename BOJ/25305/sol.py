import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 25305
# 작성 코드 시작

def solve(n, k):
    arr = list(map(int, input().split()))
    if n == k:
        return min(arr)
    return sorted(arr, reverse=True)[k - 1]

_n, _k = map(int, input().split())
print(solve(_n, _k))