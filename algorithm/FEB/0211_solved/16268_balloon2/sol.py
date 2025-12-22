import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 배열을 입력
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 순회 방향 지정(상하좌우 한칸만 확인하면 끝)
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 최대값 확인
    max_val = 0
    for i in range(N):
        for j in range(M):
            # 풍선 꽃가루 수 확인용(임시)
            temp = 0
            for dx, dy in dxy:
                # 현재 위치 + 순회 방향 지정
                ni = i + dx
                nj = j + dy
                # 인덱스 범위를 초과하지 않을 때만 꽃가루 수 확인
                if 0 <= ni < N and 0 <= nj < M:
                    temp += arr[ni][nj]
            # 자기 자리도 더함(dxy 변수에 [0, 0] 추가해도 무관)
            temp += arr[i][j]
            if max_val < temp:
                max_val = temp
    print(f'#{tc} {max_val}')
