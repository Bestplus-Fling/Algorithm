N = int(input())
matrix = [input() for _ in range(N)]
for arr in matrix:
    score = 0
    temp = 0
    for token in arr:
        if token == 'O':
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)

    import itertools
    itertools.combinations()