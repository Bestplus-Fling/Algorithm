from itertools import combinations

arr = [int(input()) for _ in range(9)]
_list = combinations(arr, 7)

for comb in _list:
    if sum(comb) == 100:
        result = comb
        break

for i in sorted(result):
    print(i)
