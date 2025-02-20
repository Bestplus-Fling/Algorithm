a = '123 345 456'
que =[]
temp =[]
for i in a:
    if i == ' ':
        temp.append(int(''.join(que)))
        que = []
        continue
    que.append(i)
temp.append(''.join(que))
print(temp)