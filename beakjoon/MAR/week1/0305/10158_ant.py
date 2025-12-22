W, H = map(int, input().split())
P, Q = map(int, input().split())
T = int(input())

tx = P + T
ty = Q + T
if (tx // W) % 2 == 0:
    ax = tx % W
else:
    ax = W - (tx % W)

if (ty // H) % 2 == 0:
    ay = ty % H
else:
    ay = H - (ty % H)

print(ax, ay)
# 배열 순서는 (1, 1), (1, -1), (-1, -1), (-1, 1)
# dx, dy = 1, 1
# idx = 0
# # 주어진 시간동안 순회
# for t in range(T):
#     # 현재 dxy[인덱스]의 진행방향을 언패킹
#     x = x + dx
#     y = y + dy
#     # 진행방향으로 계속 가다가 개미가 벽에 부딛히면
#     if not 0 < x <= W-1:
#         dx = 1 if dx < 0 else -1
#     if not 0 < y <= H-1:
#         dy = 1 if dy < 0 else -1
