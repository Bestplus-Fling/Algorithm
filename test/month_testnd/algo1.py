import sys
sys.stdin = open('algo1.txt', 'r')
#########################################

T = int(input())
for tc in range(1, T+1):
    N, i = map(int, input().split())
    charges = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    ans, energy = 0, 0

    for _ in range(N):
        # 나루터에서 충전
        energy += charges[i]
        # 에너지 소모량 제외
        energy -= costs[i]
        # 했을 때 음수이면 종료
        if energy < 0:
            energy = -1
            break
        # 음수 아닐 경우 다음 나루터로 이동
        i += 1
        if i >= N:
            i = 0

    print(f'#{tc}', energy)
