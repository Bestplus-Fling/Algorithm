# now가 target보다 작으면 = target - now
# 반대라면 = now - target

import sys
sys.stdin = open("1408.txt")

_l = [list(map(int, input().split(':'))) for _ in range(2)]
t = _l[0]
ct = _l[1]

if t[0] > ct[0]:
    ct[0] += 24
temp = (ct[0] * 3600 + ct[1] * 60 + ct[2]) - (t[0]*3600 + t[1]*60 + t[2])

h, m = divmod(temp, 3600)
m, s = divmod(m, 60)

print(f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}')
