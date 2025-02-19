import sys
sys.stdin = open('input.txt', 'r')
#########################################

"""
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때
연속인 숫자가 3개 이상이면, run, 같은 숫자가 3개 이상이면 tirplet이다.
게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며,
6장을 채우기 전이라ㄱ도 먼저 run이나 triplet이 되는 사람이 승자
무승부인 경우 0을 출력"""
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1, p2 = {}, {}
    winner = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            p1[arr[i]] = p1.get(arr[i], 0) + 1
        else:
            p2[arr[i]] = p2.get(arr[i], 0) + 1
        for j in range(1, 9):
            if p1.get(j, 0) >= 3 or (p1.get(j-1, 0) > 0 and p1.get(j, 0) > 0 and p1.get(j+1, 0) > 0):
                winner = 1
            if p2.get(j, 0) >= 3 or (p2.get(j-1, 0) > 0 and p2.get(j, 0) > 0 and p2.get(j+1, 0) > 0):
                winner = 2
        if winner:
            break
    # print(p1, p2)
    print(f'#{tc} {winner}')
