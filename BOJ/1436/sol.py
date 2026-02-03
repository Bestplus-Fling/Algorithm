import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 1436
# 작성 코드 시작

n = int(input())
count = 0
num = 666
while True:
    if '666' in str(num):
        count += 1
    if count == n:
        print(num)
        break

    num += 1


