import sys
sys.stdin = open('input.txt', 'r')
#####################################

"""
1. 첫 번째 줄은 항상 숫자 1
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 입력이 0인 경우는 없으니까 무조건 1추가하고 시작
    ans = [[1]]
    for i in range(N-1):
        # i + 2 만큼의 길이를 가진다.
        arr = [0] * (i + 2)
        for j in range(len(arr)):
            # 오른쪽 대각선 있으면 추가
            if j < len(ans[i]):
                arr[j] = ans[i][j]
            # 왼쪽 대각선이 있으면 추가 (그냥 1로 바뀜)
            if j-1 >= 0:
                arr[j] += ans[i][j-1]
        # 한 줄 완성할때마다 ans에 추가
        ans.append(arr)
    print(f'#{tc}')
    # 출력
    for i in ans:
        print(*i)


