import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    pass
# 자 그러면 첫 풍선에 가루가 한개면 상하좌우로 한칸 n개면 n칸에 있는
# 풍선안의 꽃가루의 개수를 세면 될듯

    N, M = map(int, input().split())
    my_list = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for i in range(N):
        for j in range(M):
            max_val = 0
            for k in range(my_list[i][j]):
                for dx, dy in dxy:
                    ni = i + dx * k
                    nj = j + dy * k

                    if 0 <= ni < N and 0 <= nj < M:
                        max_val += my_list[ni][nj]
            max_val += my_list[i][j]
            if max_num <= max_val:
                max_num = max_val

    print(max_num)


#

