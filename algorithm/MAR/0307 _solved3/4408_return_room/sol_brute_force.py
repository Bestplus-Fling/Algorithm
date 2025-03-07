import sys
sys.stdin = open('input.txt', 'r')
#####################################

top_room = [i for i in range(1, 400, 2)]
bottom_room = [i for i in range(2, 401, 2)]


def check(start, end):
    direction = 1 if start < end else -1
    # print(start, end, direction)
    FLAG = False
    for i in range(start, end+1, direction):
        if visited[i]:
            FLAG = True
        visited[i] = True
    return FLAG


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = [tuple(map(int, input().split())) for _ in range(N)]
    # print(students)
    visited = [False] * 400
    ans = 1
    for student in students:
        if check(student[0], student[1]):
            ans += 1

    print(f'#{tc}', ans)
