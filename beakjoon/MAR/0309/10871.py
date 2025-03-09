N, X = map(int, input().split())
_list = list(map(int, input().split()))
for num in _list:
    if num < X:
        print(num, end=' ')
print()
