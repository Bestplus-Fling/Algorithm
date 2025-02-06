import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = 10 #int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 배열을 순회했을 때 행/열/대각선의 합을 저장할 리스트 선언
    _list = []
    # 대각선 합 구하는 변수 생성
    right_diagonal, left_diagonal = 0, 0
    for i in range(100):
        # 수직, 수평 합 구하는 변수 생성
        horizen, vertical = 0, 0
        '''
        행, 열의 값이 동일한 배열에서의 대각선은 [0][0],[1][1]처럼
        x,y의 증감이 같으므로 오른쪽 대각의 합은 [i][i]이지만 
        왼쪽 대각의 합은 0,99부터 99,0까지 x는 증가, y는 감소하므로 [i][99-i]
        '''
        right_diagonal += arr[i][i]
        left_diagonal += arr[i][99-i]
        for j in range(100):
            '''
            수평의 합은 i 고정 j 증가 [0][0~99]
            수직의 합은 j 증가 i 고정 [0~99][0]
            '''
            horizen += arr[i][j]
            vertical += arr[j][i]
        # 합들을 _list에 저장
        _list.extend([horizen, vertical])
    _list.extend([right_diagonal, left_diagonal])
    #_list의 최대값을 출력
    print(f"#{N} {max(_list)}")