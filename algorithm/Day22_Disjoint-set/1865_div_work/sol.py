import sys
sys.stdin = open("output.txt", "r")
output = [input() for _ in range(100)]
ans = []
sys.stdin = open("input.txt", "r")


def f(visited, probability, row=0):
    global result
    if result > probability:
        return
    if row == N:
        result = probability
        return
    for col in range(N):
        if visited[col]: continue
        if percent[row][col] == 0: continue
        visited[col] = True
        f(visited, probability * (percent[row][col] / 100), row + 1)
        visited[col] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    f([False] * N, 100)
    print(f'#{tc} {result:.6f}')

#     ans.append(f'#{tc} {result:.6f}')
# num = 0
# for tc in range(T):
#     if ans[tc] == output[tc]:
#        num += 1
# print(num)
