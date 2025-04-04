import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
1. 지붕은 수평 부분과 수직 부분으로 구성, 모두 연결되어야 한다.
2. 지붕의 수평 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
4. 지붕의 가장자리는 땅에 닿아야 한다.
5. 비가 올때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다. 
"""
# print(arr)
# 가장 높은 기둥에서 떨어질때는 그 다음으로 가장 큰 높이를 기준으로 수평을 이룬다.
#
"""
현재 기둥을 기준으로 큰 기둥을 만나면 큰 기둥 인덱스 전까지 현재 기둥 높이로 리스트에 저장

현재 기둥을 기준으로 큰 기둥이 없다면, 다음으로 오는 기둥 중에서 가장 큰 기둥 높이로 리스트에 저장
"""
# T = int(input())   # Test case 개수를 받아오는 코드
# for tc in range(1, T+1):
N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)])
matrix = []
k = 0
prev_height = 0
while k != N:
    # 현재 확인 중인 인덱스와 기둥 높이를 언패킹
    index, height = arr[k]
    # i가 확인 중인 인덱스에 미치지 못했다면 continue
    # 기둥 리스트에서 현재 기둥보다 높은 기둥까지 거리(next_index)를 확인
    next_index = -1
    # N: 배열의 길이, 5256_binomial coefficient: 배열을 순회중인 인덱스
    # 현재 인덱스에서 다음 인덱스까지의 거리를 측정
    for j in range(k, N-k):
        if arr[j][1] > height:
            next_index = arr[j][0]
            break
    if height > prev_height:
        prev_height = height
        if next_index != -1:
            matrix.extend([height] * (next_index - index))
        # 현재 기둥 높이보다 높은 기둥이 없다면 현재 기둥을 제외하고 가장 높은 기둥을 측정
        else:
            temp, idx = 0, 0
            for j in range(k+1, N):
                # print(arr[j])
                if temp < arr[j][1]:
                    temp = arr[j][1]
                    idx = arr[j][0]
            # 현재 기둥높이와, 다음으로 가장 높은 기둥까지의 값을 matrix에 저장
            matrix.append(height)
            # print(temp, idx)
            matrix.extend([temp] * (idx - index))
    k += 1
print(sum(matrix))
