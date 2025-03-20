import sys
sys.stdin = open('input.txt', 'r')
#####################################
import heapq


T = int(input()) # test case개수를 받아오는 코드
for tc in range(1, T+1):
    N, A = map(int, input().split())
    heap1, heap2 = [A], []
    mid = A
    ans = 0
    for _ in range(N):
        #mid를 기준으로 큰 값은 heap1, 작거나 같은 값은 heap2
        x, y = map(int, input().split())
        if x > mid:
            heap1.append(x)
        else:
            heap2.append(-x)

        if y > mid:
            heap1.append(y)
        else:
            heap2.append(-y)
        heapq.heapify(heap1)
        heapq.heapify(heap2)
        print(heap1, heap2)
        while len(heap1) < len(heap2):
            temp = -heapq.heappop(heap2)
            heapq.heappush(heap1, temp)
            print(heap1, heap2)
            print()
        # print(heap1, heap2)
        mid = heap1[0]
        print(mid)

    print(f'#{tc}', ans)