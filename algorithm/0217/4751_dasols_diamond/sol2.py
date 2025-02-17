import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 문자를 입력 받는다.
    word = input()
    # 문자를 꾸밀 최종 너비를 구한다.
    width = (len(word) * 5) - (len(word) - 1)
    # 문자열을 순회할 수 있도록 인덱스용 변수를 선언
    word_index = 0
    for i in range(5):
        # 한 줄의 너비만큼 순회
        for j in range(width):
            # 문자가 출력되는 행(i == 2)에서
            if i == 2:
                # #의 위치는 0, 4, 8, ... 형태로 4배씩 증가
                if j % 4 == 0:
                    print('#', end='')
                    continue
                # 문자가 출력되는 위치는 2, 6, 10, 14 ... 형태
                elif j == 2 or (j != 0 and (j-2) % 4 == 0):
                    print(word[word_index], end='')
                    # 문자 하나를 출력하면 인덱스 += 1
                    word_index += 1
                    continue
            # 1, 3행에서
            elif i % 2 != 0:
                # #의 위치는 1, 3, 5, 7, 9... 홀수에서만 출력
                if j % 2 != 0:
                    print('#', end='')
                    continue
            # 0, 4행에서
            else:
                # #의 위치는 i == 2행에서 문자가 출력되는 위치와 동일
                if j == 2 or (j != 0 and (j-2) % 4 == 0):
                    print('#', end='')
                    continue
            # 모든 경우가 아니면 dot(.)을 출력
            print('.', end='')
        # 한 행이 끝나면 줄바꿈 실행
        print()
