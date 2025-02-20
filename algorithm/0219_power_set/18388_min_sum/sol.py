import sys
sys.stdin = open('input.txt', 'r')
#########################################


def is_min(idx, num_sum, prev):
    global _min
    # 최소합보다 이미 커진 순간 early return
    if num_sum >= _min:
        return
    # depth(idx)가 배열 크기(N)과 같아진다면(=모든 행에 대한 순회가 종료되면)
    if idx == N:
        # 최소값 확인 후 갱신
        _min = min(_min, num_sum)
        return
    # 현재 행을 순회, j열에 위치한 원소를 선택하면 j를 제약조건으로 설정(prev)
    for j in range(N):
        # prev 리스트에 j열 요소를 선택한 적이 없을 때 다음 행을 탐색
        if j not in prev:
            prev.append(j)
            is_min(idx + 1, num_sum + matrix[idx][j], prev)
            # 다음 열을 선택하면 현재 열이 제약 조건으로 포함되면 안되므로 제약 조건 제거
            prev.pop()


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # matrix의 크기를 입력
    N = int(input())
    # N * N의 숫자 입력
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 배열 최소합 저장 변수 생성
    _min = float('inf')
    # 배열 최소합을 찾는 함수 호출
    is_min(0, 0, [])
    print(f'#{tc}', _min)

