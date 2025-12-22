numbers = list(range(1, 11))
answer = []
for i in range(1 << 10):
    tmp = []
    for j in range(10):
        if i & (1 << j):
            tmp.append(numbers[j])
    answer.append(tmp)
print(answer)