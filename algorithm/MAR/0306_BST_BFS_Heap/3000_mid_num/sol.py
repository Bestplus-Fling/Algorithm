import sys
sys.stdin = open('input.txt', 'r')
#####################################
import heapq

T = int(input()) # test case개수를 받아오는 코드
for tc in range(1, T+1):
    N, A = map(int, input().split())
    # heap1 최대힙으로 사용, heap2 최소힙으로 사용(중간값이 맨 앞에 있음)
    heap1, heap2 = [], [A]
    # 중간값 선언
    mid = A
    ans = 0
    for _ in range(N):
        #mid를 기준으로 작은 값은 heap1에, 크거나 같은 값은 heap2에 삽입
        x, y = map(int, input().split())
        if x < mid:
            heapq.heappush(heap1, -x)
        else:
            heapq.heappush(heap2, x)

        if y < mid:
            heapq.heappush(heap1, -y)
        else:
            heapq.heappush(heap2, y)

        # 비대칭의 비율은 heap2 길이 - heap1의 차가 1이여야 한다.
        while len(heap2)-len(heap1) != 1:
            # heap2가 더 많으면 heap1에 음수 붙여서 삽입
            if len(heap2) > len(heap1):
                heapq.heappush(heap1, -heapq.heappop(heap2))
            # heap1이 더 많으면 heap2에 음수 붙여서 삽입
            else:
                heapq.heappush(heap2, -heapq.heappop(heap1))
        # 자료 정리 후 중간값 갱신(중간값은 heap2의 가장 앞에 있는 값)
        mid = heap2[0]
        ans += mid
        ans %= 20171109

    print(f'#{tc}', ans)
