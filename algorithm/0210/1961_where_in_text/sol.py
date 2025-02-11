import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    list_ = []
    rotate_90 = list(zip(*arr[::-1]))
    list_.append(rotate_90)

    rotate_180 = list(zip(*rotate_90[::-1]))
    list_.append(rotate_180)

    rotate_270 = list(zip(*rotate_180[::-1]))
    list_.append(rotate_270)
    print(f'#{tc}')
    for x in range(N):
        for i in range(3):
            temp = ''
            for j in range(N):
                temp += str(list_[i][x][j])
            print(temp, end=' ')
        print()
