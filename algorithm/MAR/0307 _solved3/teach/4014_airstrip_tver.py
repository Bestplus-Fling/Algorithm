import sys
sys.stdin = open('4014.txt', 'r')
#####################################\


# 어떤 행이 들어왔을 때, 해당 행에 활주로를 건설할 수 있는 지 검사하는 함수
# return True => 활주로 건설 가능
# return False => 활주로 건설 불가
def inspect_road(road):
    visited = [False] * N
    # 현재 칸을 기준으로 다음 칸과 높이를 비교한다.
    for idx in range(N-1):
        # 높이 차를 구해준다
        h_diff = abs(road[idx] - road[idx + 1])

        # 높이 차이가 안나는 경우
        if h_diff == 0: continue

        # 높이 차이가 2 이상 발생하는 경우 종료
        if h_diff >= 2: return False
        # 높이 차이가 1인 경우, 경사로를 설치할 수 있는지 확인
        # 높이가 낮아지는 경우
        if road[idx] > road[idx + 1]:
            ct_h = road[idx + 1]
            # 검사 범위를 설정
            search_list = range(idx + 1, N)
        # 높이가 높아지는 경우
        else:
            ct_h = road[idx]
            search_list = range(idx, -1, -1)
        # 경사로 설치 구간에 설치할 수 있는 지 확인
        # 설치 조건 1: 높이가 일정해야 한다
        for load_cnt, jdx in enumerate(search_list):
            if road[jdx] != ct_h: return False
            # 이미 설치된 경우
            if visited[jdx]: return False

            # 설치 가능
            visited[jdx] = True

            if load_cnt + 1 == X:
                break
        # 아래 else에 도달했다 => break 가 실행되지 않았다
        # => x 만큼 설치되지 않았다.
        else:
            return False
    # 여기까지 왔다 => 활주로를 무사히 건설했다.
    return True


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 활주로를 건설할 수 있는 경우의 수

    # 1. 각 행에 대해서 활주로 검사를 시작
    # 2. 주어진 matrix 90도 회전
    # 3. 회전한 matrix 의 각 행에 대해서 다시 활주로 검사를 한다
    for ar in arr:
        if inspect_road(ar):
            # print(ar)
            result += 1
    rotate_arr = list(zip(*arr))

    for rot_ar in rotate_arr:
        if inspect_road(rot_ar):
            # print(rot_ar)
            result += 1
    print(f'#{tc}', result)
    # break