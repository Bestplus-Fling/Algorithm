import math

# 두 점의 위치
start = (2, 0)
target = (2, -2)

x = target[0] - start[0]
y = target[1] - start[1]

distence = math.dist(target, start)
print(distence)

theta = math.degrees(math.atan2(y, x))
print(theta)
out = abs(theta - 90)
print(out)


# 현재 위치
Ax, Ay = 0, 0
points = [
    (1, 2),
    (-2, -3),
    (3, 1),
    (-1, 4)
]
dist_list = []
for i in range(len(points)):
    dist_list.append(math.dist(points[i], start))
print(dist_list)

print(math.cos(60))
