import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    # N:배열의 길이(가로/세로 동일) K: 문자길이
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 문자길이만큼 1이 있는 공간을 count
    check = 0
    # 가로 순회
    for row in puzzle:
        # 1의 개수 확인
        ans = 0
        # 순회하고 있는 가로에 1의 개수가 K개 만큼 있을 때
        if row.count(1) >= K:
            # 행 내부를 순회
            for i in range(N):
                # 행에 1이 있을 때마다 cnt++
                if row[i] == 1:
                    ans += 1
                # 0을 만나면 cnt 초기화
                else:
                    ans = 0
                '''
                조건1: 1의 개수가 K개만큼 있다 그리고(and)
                조건2-1: 인덱스가 종점에 위치했거나(or)
                조건2-2: 인덱스가 종점에 위치하지 않고(and)
                현재 순회중인 row 다음 인덱스가 0일 경우
                '''
                ''' 설명
                cnt가 K만큼 누적했다고 해도 다음 숫자가 1이면 count하지 않음.
                다음 칸에 0이여서 초기화되기까지의 결과가 K와 동일하다면
                check++

                인덱스의 순회가 끝나서 다음칸이 없을 경우(out of range) 
                정상적으로 cnt된거니까 check++
                '''
                if ans == K and (i == N - 1 or (i + 1 < N and row[i + 1] == 0)):
                    check += 1
                    ans = 0
                    continue
            # 행과 동일한 형태, 열을 확인하기 위해 리스트를 새로 생성해서 순회
    for j in range(N):
        col = []
        for _ in range(N):
            col.append(puzzle[_][j])
        ans = 0

        if col.count(1) >= K:
            for i in range(N):
                if col[i] == 1:
                    ans += 1
                else:
                    ans = 0
                if ans == K and (i == N - 1 or (i + 1 < N and col[i + 1] == 0)):
                    check += 1
                    ans = 0
                    continue
    print(f'#{tc} {check}')
