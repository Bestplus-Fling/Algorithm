import sys
sys.stdin = open('input.txt', 'r')
#########################################
def is_palindrme(word, left, right):
    if left >= right:
        return 1
    if word[left] != word[right]:
        return 0

    return is_palindrme(word, left + 1, right - 1)

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    word = input()
    len_w = len(word)

    print(f'#{tc} {is_palindrme(word, 0, len_w - 1)}')