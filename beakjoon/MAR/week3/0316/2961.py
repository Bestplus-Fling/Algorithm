import sys
sys.stdin = open('input/2961_1.txt', 'r')
#########################################


def select_taste(idx, sum_sour=1, sum_bitter=0):
    global result
    taste = abs(sum_bitter - sum_sour)
    if idx == N:
        if sum_sour != 1 and sum_bitter != 0:
            result = min(taste, result)
        return
    select_taste(idx+1, sum_sour*sour_list[idx], sum_bitter+bitter_list[idx])
    select_taste(idx+1, sum_sour, sum_bitter)


N = int(input())
sour_list, bitter_list = [], []
for i in range(N):
    S, B = map(int, input().split())
    sour_list.append(S)
    bitter_list.append(B)
result = 1000000001
select_taste(0)
print(result)
