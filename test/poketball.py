import math

# 두 점의 위치
start = (2, 0)
target = (2, -2)

x = target[0] - start[0]
y = target[1] - start[1]

theta = math.degrees(math.atan2(y, x))
print(theta)
out = abs(theta - 90)
print(out)


# 현재 위치
Ax, Ay = 0, 0
