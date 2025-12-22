"""
1. 등장하는 모든 원소의 종류를 파악
    파악한 원소들을 오름차순으로 정렬

2. 한 종류의 원소에 대해 그 원소에 가장 빠른 등장위치 파악
"""

N = int(input())
arr = list(map(int, input().split()))

# 등장하는 모든 원소의 종류를 파악 + 오름차순 정렬
# set을 이용
unique_items = sorted(list(set(arr)))

# first 제작
first = {}
for idx, value in enumerate(arr, start=1):
    if value not in first:
        first[value] = idx

# # side note
# for idx in range(len(arr)-1, -1, -1):
#     first[arr[idx]] = [idx]

# 각 원소에 대해 첫 등장 위치를 파악
# map을 사용, fist[i]: i의 첫 등장 위치
for item in unique_items:
    print(item, first[item])