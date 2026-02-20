import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/1817
# 작성 코드 시작

def solve():
    n, m = map(int, input().split())
    if n == 0:
        return 0
    books = list(map(int, input().split()))
    box = 0
    ret = 1

    for book in books:
        if box + book <= m:
            box += book
        else:
            ret += 1
            box = book
    return ret

print(solve())