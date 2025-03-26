import sys
sys.stdin = open('input/10816.txt', 'r')
#########################################
"""
매번 정리할 수 없음
그렇다고 인덱스 접근도 불가능
딕셔너리로 정리?
"""

# def bst(num):
#     left, right = [], []
#     for i in a:
#         if i
from collections import defaultdict
dic = defaultdict(int)
N = int(input())
a = sorted(list(map(int, input().split())))
for i in a:
    dic[i] += 1
M = int(input())
c = list(map(int, input().split()))
ans = []
for j in c:
    ans.append(dic[j])
print(*ans)
