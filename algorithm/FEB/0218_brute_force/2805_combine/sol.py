import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
농장의 크기(N)은 항상 홀수
수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태만 가능
'''
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    center = N//2
    width, ans = 0, 0
    for i in range(N):
        for j in range(center-width, center+width+1):
            ans += int(arr[i][j])
        width += 1 if i < center else -1
    print(f'#{tc}', ans)
