import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())  # 연속된 문자열(숫자)를 입력
    temp = input()  # 딕셔너리 변수 생성
    _dict = {}
    for x in temp:  # temp를 순회
        if x in _dict:  # x가 _dict에 이미 존재하면 value 증가
            _dict[x] += 1
        else:  # x가 한번도 정의되지 않았다면 1 부여
            _dict[x] = 1
        max_num = str(x) # 가장 마지막에 선언된 key를 max_num에 임의로 지정
        ''' 한 for문에서 판별 종료(사용시 for idx 부터 max_num = idx까지 주석처리 바랍니다)
        if x == temp[0]:
            max_num = x
        if _dict[x] >= _dict[max_num] and x > max_num:
            max_num = x
        '''
    # _dict 내 value가 가장 큰 key 중에 가장 큰 값(동일한 value에서 가장 key값이 우선)
    for idx in _dict:
        # value가 일치하더라도 key의 숫자가 더 크면 max_num 변경
        if _dict[idx] >= _dict[max_num] and idx > max_num:
            max_num = idx
    print(f'#{tc} {max_num} {_dict[max_num]}')
