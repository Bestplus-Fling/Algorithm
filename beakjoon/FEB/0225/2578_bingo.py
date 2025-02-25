# input
"""
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
"""

"""
문제 1: 빙고 위치를 확인하려고 이중 for 문을 또 돌려야 함
문제 2: for 문 돌아간다고 확인할 수 있는 방법이 없음
문제 3: zip 으로 전치 돌리고 확인, 그냥 정방향으로 확인, 바깥 for문에서 [i][i], [i][4-i]
"""


def around_list():
    count = 0
    for k in range(5):
        arr = list(map(int, input().split()))
        for idx in range(5):
            for i in range(5):
                for j in range(5):
                    if matrix[i][j] == arr[idx]:
                        matrix[i][j] = 0
                        count += 1
                        if search_bingo():
                            return count


def search_bingo():
    cnt1, cnt0 = 0, 0
    check = 0
    for n in range(5):
        cnt0 += 1 if not matrix[n][n] else 0
        cnt1 += 1 if not matrix[n][4-n] else 0
        cnt2, cnt3 = 0, 0
        for m in range(5):
            cnt2 += 1 if not (matrix[n][m]) else 0
            cnt3 += 1 if not (matrix[m][n]) else 0
        check += 1 if cnt2 == 5 else 0
        check += 1 if cnt3 == 5 else 0
        if check >= 3:
            return True
    check += 1 if cnt0 == 5 else 0
    check += 1 if cnt1 == 5 else 0

    return True if check >= 3 else False


matrix = [list(map(int, input().split())) for _ in range(5)]

temp = around_list()
print(temp)


