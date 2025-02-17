import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    word = input()
    width = (len(word) * 5) - (len(word) - 1)
    word_index = 0
    for i in range(5):
        for j in range(width):
            if i == 2:
                if j % 4 == 0:
                    print('#', end='')
                    continue
                elif j == 2 or (j != 0 and (j-2) % 4 == 0):
                    print(word[word_index], end='')
                    word_index += 1
                    continue
            elif i % 2 != 0:
                if j % 2 != 0:
                    print('#', end='')
                    continue
            else:
                if j == 2 or (j != 0 and (j-2) % 4 == 0):
                    print('#', end='')
                    continue
            print('.', end='')
        print()
