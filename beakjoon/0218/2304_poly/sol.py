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
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = sorted([tuple(map(int, input().split())) for _ in range(N)])
    matrix = []
    print(arr)
    j = 0
    # 가장 높은 기둥에서 떨어질때는 그 다음으로 가장 큰 높이를 기준으로 수평을 이룬다.
    #
    """
    현재 기둥을 기준으로 큰 기둥을 만나면 큰 기둥 인덱스 전까지 현재 기둥 높이로 리스트에 저장
    
    현재 기둥을 기준으로 큰 기둥이 없다면, 다음으로 오는 기둥 중에서 가장 큰 기둥 높이로 리스트에 저장
    """
    for i in range(arr[0][0], arr[-1][0]+1):
        index, height = arr[j]
        if i == index:
            pass
            j += 1
        else:
            pass
