import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    pass
# 자 그러면 첫 풍선에 가루가 한개면 상하좌우로 한칸 n개면 n칸에 있는
# 풍선안의 꽃가루의 개수를 세면 될듯

    N, M = map(int,input().split())
    my_list = [list(map(int,input().split())) for _ in range(N)]

    max_num = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            max_value = []
            for k in range(my_list[i][j]):
                for l in range(4):
                    if dx[l] > 0:
                        ni = i + dx[l] + k
                    elif dx[l] < 0:
                        ni = i + dx[l] - k
                    else:
                        ni = i + dx[l]

                    if dy[l] > 0:
                        nj = j + dy[l] + k
                    elif dy[l] < 0:
                        nj = j + dy[l] - k
                    else:
                        nj = j + dy[l]

                    if 0 <= ni < N and 0 <= nj < M:
                        max_value.append(my_list[ni][nj])
            max_value.append(my_list[i][j])
            if max_num <= sum(max_value):
                max_num = sum(max_value)

    print(max_num)


#

