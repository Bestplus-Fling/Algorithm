import sys
sys.stdin = open('test.txt', 'r')
# sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    # 이동한 경로를 확인
    visited = [0 for _ in range(202)]
    N = int(input())
    for i in range(N):
        # 현재 방 위치, 도착하려는 방 위치 입력
        start, end = map(int, input().split())
        # 도착하려는 방 번호가 더 작은 경우, 시작, 끝 위치를 바꾼다
        if start > end:
            start, end = end, start
        # 홀수번 방, 홀수번 + 1(짝수) 방은 마주봐야 한다.
        start = start // 2 + start % 2
        end = end // 2 + end % 2
        # 이동 경로의 교집합을 확인
        for j in range(start, end+1):
            visited[j] += 1
    # 교집합의 최대값(기다려야 하는 단위시간)을 출력
    print(f'#{tc}', max(visited))
