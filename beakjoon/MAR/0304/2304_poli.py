N = int(input())
piller_list = sorted([tuple(map(int, input().split())) for _ in range(N)])
# 가장 높은 기둥 위치 찾기
max_h = 0
for i, h in piller_list:
    if max_h < h:
        max_piller = (i, h)
        max_h = h
idx = 0
area = []
now_height = piller_list[idx][1]
for i in range(piller_list[0][0], max_piller[0]+1):
    # 다음 기둥이 있는 위치까지 현재 기둥으로 채우기
    next_index = piller_list[idx+1][0]

    # 현재 위치가 다음 기둥이 있는 위치라면 idx += 1,
    # 높이를 갱신
    if next_index == i:
        idx += 1
        if piller_list[idx][1] > now_height:
            now_height = piller_list[idx][1]
    area.append(now_height)
# print(idx, area)
n = idx
for i in range(piller_list[n][0], piller_list[-1][0]):
    #가장 높은 기둥을 제외한 나머지 기둥 중 가장 높은 기둥이 있는 위치까지 채운다.
    target_piller = 0
    max_h = 0
    if next_index == i:
        idx += 1
        for j in range(idx, N):
            if piller_list[j][1] > max_h:
                max_piller = (piller_list[j][0], piller_list[j][1])
                max_h = piller_list[j][1]
        next_index = max_piller[0]
        now_height = max_piller[1]
    area.append(now_height)
print(sum(area))


