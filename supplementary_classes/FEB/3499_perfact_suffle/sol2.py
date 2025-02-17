import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    word_list = list(input().split())
    output = []
    for i in range(N):
        output.append(word_list[i//2 + ((N//2 + N % 2) * (i % 2))])
    print(f"#{tc} {' '.join(output)}")
