import sys
sys.stdin = open('input.txt', 'r')
#########################################

from itertools import permutations

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    arr = list(map(int, input().strip()))
    for tp in list(set(permutations(arr, 3))):
        count = 0
        for i in tp:
            if i in arr:
                count += 1
        if count == 3:
            print(2)
        # while [a, b, c] in arr:
        #     print(1)
        #     if a == b == c or a+1 == b == c-1:
        #         print(tp)
        #         arr.remove(a)
        #         arr.remove(b)
        #         arr.remove(c)
        #     break
        # print(arr)
    break