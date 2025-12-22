import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    word = input()
    check = 1
    for idx in range(len(word)//2):
        if word[idx] != word[len(word) - 1 - idx]:
            check = 0
            break
    print(f'#{tc} {check}')
