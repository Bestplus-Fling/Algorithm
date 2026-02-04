import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 14646
# 작성 코드 시작

n = int(input())
arr = list(map(int, input().split()))

sticker = [False] * (n + 1)
max_cnt = 0
cnt = 0
for i in range(len(arr)):
    menu = arr[i]
    if sticker[menu]:
        max_cnt = max(cnt, max_cnt)
        cnt -= 1
    else:
        sticker[menu] = True
        cnt += 1
print(max_cnt)