import sys
sys.stdin = open('input.txt', 'r')


N = int(input())        # 스위치 개수
# 스위치 초기 상태
switch = list(map(int, input().split()))
cnt_student = int(input())
list_student = [tuple(map(int, input().split())) for _ in range(cnt_student)]

for mf, idx in list_student:
    print(switch)
    if mf == 1:
        for i in range(idx-1, N, idx):
            switch[i] = (0 if switch[i] == 1 else 1)
    else:
        switch[idx-1] = 0 if switch[idx-1] == 1 else 1

        for k in range(1, N//2):
            val1 = idx-1 + k
            val2 = idx-1 - k
            if not(0 <= val2 and val1 < N):
                break
            if switch[val1] == switch[val2]:
                switch[val1] = (0 if switch[val1] == 1 else 1)
                switch[val2] = (0 if switch[val2] == 1 else 1)
                continue
            else:
                break

for i in range(1, N+1):
    print(switch[i-1], end=' ')
    if i % 20 == 0:
        print()
