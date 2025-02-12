import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    word = input()
    check_list = ['']

    for txt in word:
        if check_list[-1] != txt:
            check_list.append(txt)
            continue
        else:
            check_list.pop()
    check_list.pop(0)

    print(f"#{tc} {len(check_list)}")



