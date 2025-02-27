# a b가 딱지놀이를 한다
# 여러 장의 딱지를 가지고 있고 딱지 중 어느 쪽이 더 강력한 것인지 규칙을 따른다.

# 두 딱지의 별의 개수가 다르면, 별이 많은 쪽의 딱지가 이긴다.
# 별의 개수가 같고 동그라미의 개수가 다르면, 동그라미가 많은 쪽의 딱지가 우승
# 별, 동그라미의 개수가 동일, 네모의 개수가 다르면, 네모가 많은 쪽의 딱지 우승
# 별, 동그라미, 네모의 개수가 다르면 세모의 개수가 많은 쪽의 딱지 우승
# 모두 같다면 무승부(D를 출력)

# 4: 별, 3: 동그라미, 2: 네모, 1: 세모
import sys
sys.stdin = open('scab.txt', 'r')
#########################################



N = int(input())

for i in range(N):
    a, *ai = map(int, input().split())
    b, *bi = map(int, input().split())
    if a == b:
        au, bu = sorted(ai), sorted(bi)
        if au == bu:
            print('D')
            continue
    for j in range(4, 0, -1):
        an, bn = ai.val_TF(j), bi.val_TF(j)
        if an == bn:
            continue
        if an > bn:
            print('A')
            break
        elif an < bn:
            print('B')
            break