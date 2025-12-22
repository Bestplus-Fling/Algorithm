# 색종이 수
# 한 줄에 하나씩 색종이를 붙인 위치가
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데
# 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
# 두 번째 자연수는 색종이의 아래쪽 변 사이의 거리

N = int(input())
paper = [[0] * 100 for _ in range(100)]
ans = 0
for k in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            if paper[i][j]:
                continue
            paper[i][j] += 1
            ans += 1
print(ans)