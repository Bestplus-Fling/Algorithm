import sys
sys.stdin = open('input2_0.txt', 'r')
#########################################


N, M = map(int, input().split())
arr = list(map(int, input().split()))
"""
M 개의 비어있는 의자와 N 명의 사람이 있고 N명이 원하는 위치는
1 이상 ai 이하의 범위 안에 있는 의자

"""
dic = {}
temp = [0] * (M+1)
for i in range(N):
    dic[arr[i]] = dic.get(arr[i], 0) + 1
print(dic)
ans_a = 0
for i in range(N):
    idx = arr[i]
    if not temp[idx]:
        temp[idx] = 1
        dic[idx] -= 1
        ans_a += 1
    else:

