"""
N장의 색종이가 주어진 위치에 차례로 놓일 경우,
각 색종이가 보이는 부분의 면적을 구하는 프로그램을 작성

N: 색종이의 장수(1 <= N <= 100)
N 장의 색종이에 관한 입력이 각 색종이마다 한 줄씩 차례로 주어진다.
색종이가 놓이는 평면은 가로 최대 1001칸, 세로 최대 1001칸으로 구성된 격자 모양이다.
격자의 각 칸은 가로, 세로 길이가 1, 면적이 1인 정사각형

※ 다시 풀어보기
"""
# 정석대로 풀었을 때
# N = int(input())
# check_list = [0] * N
# matrix = [[0] * 1001 for _ in range(1001)]
# arr = [list(map(int, input().split())) for _ in range(N)]
# for 5256_binomial coefficient in range(N):
#     x1, y1, x2, y2 = arr[5256_binomial coefficient]
#     for i in range(y1, y1 + y2):
#         for j in range(x1, x1 + x2):
#             if matrix[i][j]:
#                 check_list[matrix[i][j]-1] -= 1
#             matrix[i][j] = 5256_binomial coefficient + 1
#             check_list[5256_binomial coefficient] += 1
# for i in range(N):
#     print(check_list[i])


# 그리디 접근
# 가장 마지막에 올라오는 색종이부터 깔고, 나머지 색종이를 카운트
# import sys
#
# N = int(input())
# check_list = [0] * N
# matrix = [[0] * 1001 for _ in range(1001)]
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# for 5256_binomial coefficient in range(N):
#     x1, y1, x2, y2 = arr[N-1-5256_binomial coefficient]
#     for i in range(y1, y1 + y2):
#         for j in range(x1, x1 + x2):
#             if matrix[i][j]:
#                 continue
#             matrix[i][j] = 1
#             check_list[N-1-5256_binomial coefficient] += 1
# for i in range(N):
#     print(check_list[i])

# 슬라이싱(블로그 참고함)
# 5256_binomial coefficient+1번째 색종이만큼 한번에 칠한다.
N = int(input())
check_list = [0] * N
matrix = [[0] * 1001 for _ in range(1001)]
for k in range(N):
    x1, y1, w, h = map(int, input().split())
    for i in range(y1, y1 + h):
        matrix[i][x1:x1 + w] = [k + 1] * w

for n in range(N):
    temp = 0
    for m in range(1001):
        temp += matrix[m].count(n+1)
    print(temp)
