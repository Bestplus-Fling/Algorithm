import sys
sys.stdin = open('13305.txt', 'r')

N = int(input())
road_length = list(map(int, input().split()))
road_length.append(0)
gas_station = list(map(int, input().split()))
N -= 1
low_cost = min(gas_station)
# 이동이 아예 불가능할 때,
# 앞선 주유소의 가격이 더 저렴하면 필요한 양의 기름만 주유
# 아닐 경우 그 다음 거리만큼 더 충전
gas = 0
pay = 0

for i in range(N-1):
    # 기름이 부족하면
    if gas < road_length[i]:
        # 근데 여기가 최저가 주유소라면
        if gas_station[i] == low_cost:
            # 여기서 남아있는 모든 거리를 이동할 수 있도록 기름을 채운다.
            litter = sum(road_length[i:]) - gas
            gas += litter
            pay += litter * gas_station[i]
        else:   # 최저가 주유소가 아니면 다음 주유소까지만 이동할 수 있게 한다.
            litter = road_length[i] - gas
            gas += litter
            pay += litter * gas_station[i]

    gas -= road_length[i]

    print(gas, pay)
print(pay)
