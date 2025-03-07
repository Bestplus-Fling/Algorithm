import sys
sys.stdin = open('input.txt', 'r')
#####################################

cases = {
    (1, 2): 1, (1, 3): 0,
    (2, 1): 0, (2, 3): 1,
    (3, 1): 1, (3, 2): 0,
}
# 숫자가 같을 경우 p1이 승리
# 숫자가 다를 경우
# 튜플쌍을 key로 하는 value를 받아온다. 0이면 p1이, 1이면 p2가 승리

# 분할한 player들(2명이 될때까지)을 입력받고
# 승자를 반환받아서 main으로 돌려준다.
# 이때 tuple 형태로 초기 idx랑 카드를 같이 반환한다.


def select_player(players):
    # 종료 조건: player len == 2
    # logic: tuple 형태로 카드 쌍을 cases에 넣은 value를 반환했을 때
    # idx에 위치한 player만 return됨
    if len(players) == 1:
        return players[0]
    if len(players) == 2:
        if players[0][1] == players[1][1]:
            return players[0]
        data = cases[(players[0][1], players[1][1])]
        return players[data]
    # 종료조건이 아닐 경우: player를 분할해서 재귀 호출
    _len = len(players)
    # print(players[:(_len+1) // 2])
    p1 = select_player(players[:(_len+1) // 2])
    # print(p1)
    # print(players[(_len+1) // 2:])
    p2 = select_player(players[(_len+1) // 2:])
    # print(p2)
    if p1[1] == p2[1]:
        return p1
    return p2 if cases[(p1[1], p2[1])] else p1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_list = list(map(int, input().split()))
    player = []
    for i in range(N):
        player.append((i + 1, card_list[i]))
    winner = select_player(player)
    print(f'#{tc}', winner[0])
