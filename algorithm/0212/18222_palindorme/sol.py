import sys
sys.stdin = open('input.txt', 'r')
#########################################


def check_palin(word_row, word_col):
    for j in range(N):
        stack_row1, stack_row2 = [], []
        stack_col1, stack_col2 = [], []
        if 0 <= j+M-1 < N:
            for o in range(0, M):
                if j+o < j+M-o-1:
                    stack_row1.append(word_row[j+o])
                    stack_row2.append(word_row[j+M-o-1])
                    stack_col1.append(word_col[j+o])
                    stack_col2.append(word_col[j+M-o-1])
                if o == 0:
                    rt_row = word_row[j+o:j+M-o]
                    rt_col = word_col[j+o:j+M-o]
            while stack_row1:
                if stack_row1.pop() != stack_row2.pop():
                    break
            if not stack_row1 and not stack_row2:
                return rt_row

            while stack_col1:
                if stack_col1.pop() != stack_col2.pop():
                    break
            if not stack_col1 and not stack_col2:
                return rt_col
        else:
            continue


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word_arr = [input() for _ in range(N)]
    word_list = list(zip(*word_arr[::-1]))

    for i in range(N):
        search = check_palin(word_arr[i], word_list[i])
        if search:
            break

    if type(search) is tuple:
        print(f'#{tc} {"".join(search)}')
    else:
        print(f'#{tc} {search}')
