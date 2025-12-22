n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Write your code here!
for i in range(n):
    num, dxy = points[i]
    x, y = dxy
    way = abs(x) + abs(y)
    points[i] = (way, num)

points.sort()
points.reverse()
for i in range(-1, -(n+1), -1):
    dum, num = points[i]
    print(num+1)
