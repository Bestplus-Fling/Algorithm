import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
첫 줄: 종이의 가로와 세로의 길이가 자연수로 주어진다(가로와 세로의 길이는 최대 100)
둘째 줄: 칼로 잘라야 하는 점선의 개수
셋째 줄부터 마지막 줄까지: 한 줄에 점선이 하나씩,
가로로 자르는 점선 => 0과 점선 번호
세로로 자르는 점선 => 1과 점선 번호
"""

from collections import deque

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cut_cnt = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(cut_cnt)]
    row, col = [], []
    # cross, index = arr[0]
    # first_idx = (index, M) if cross == 0 else (N, index)
    # case = [(0, 0), first_idx, (N, M)]

    for cross, index in arr:
        if cross == 0:
            row.append(index)
        else:
            col.append(index)
    row = deque(sorted(row))
    col = deque(sorted(col))
    max_wide = 0
    while True:

