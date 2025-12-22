import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    word_list = list(input().split())
    shuffle1 = deque(word_list[:N//2 + N % 2])
    shuffle2 = deque(word_list[N//2 + N % 2:])
    output = []
    for i in range(N):
        if i % 2 == 0:
            output.append(shuffle1.popleft())
            continue
        output.append(shuffle2.popleft())
    print(f"#{tc} {' '.join(output)}")
