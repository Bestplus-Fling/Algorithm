import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bug_list = [list(map(int, input().split())) for _ in range(N)]
    # print(bug_list)
    kill_bug = 0
    for x in range(N):
        for y in range(N):
            temp = 0
            for i in range(M):
                if 0 <= x+i < N:
                    for j in range(M):
                        if 0 <= y+j < N:
                            temp += bug_list[x+i][y+j]
            if temp > kill_bug:
                kill_bug = temp
    print(f'#{tc} {kill_bug}')
