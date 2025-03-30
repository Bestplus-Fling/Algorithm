import sys
sys.stdin = open('input.txt', 'r')
#########################################
import heapq

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    mh = []
    ans = []
    heapq.heapify(mh)
    for _ in range(int(input())):
        work = input().split()
        if len(work) == 2:
            heapq.heappush(mh, -int(work[-1]))
        else:
            if not mh:
                ans.append(-1)
                continue
            ans.append(-heapq.heappop(mh))
    print(f'#{tc}', *ans)
