import sys
sys.stdin = open("24416.txt")


# def fib(n):
#     global a
#     if n == 1 or n == 2:
#         return 1
#     a += 1
#     return fib(n-1) + fib(n-2)


def fibonacci(n):
    global c
    f = [1, 1]
    for i in range(2, n):
        c += 1
        f.append(f[i-1]+f[i-2])
    return f[n-1]


N = int(input())
c = 0
t = fibonacci(N)
print(t, c)




