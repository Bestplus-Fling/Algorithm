import sys
sys.stdin = open('input.txt', 'r')
#########################################
# 괄호 개폐가 인접하면 레이저
# 괄호 개폐가 인접하지 않으면 쇠막대기

# 스택 맨 아래는 제일 긴 파이프가
# 스택의 top에는 가장 짧은 파이프가 존재
# 파이프 시작과 끝을 확인하면서 증감하는 변수 필요
# 레이저가 있으면 증감 변수를 통해 각 리스트 요소를 순회하면서 값을 2배로 만들고
# 파이프의 끝단에 도달하면 top 파이프의 숫자를 pop하면서 result에 더하기

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    razer = input()
    pipe = []
    result = 0
    for i in range(len(razer)):
        token = razer[i]
        """
        괄호 삽입, 닫힌 괄호가 나오면 괄호 스택[-1] 자리 괄호 확인
        """
        # print(token)
        # 괄호가 열렸는데 인접하는 경우 레이저 확인
        if i != len(razer)-1:
            if token == '(' and razer[i+1] == ')':
                # print("razer")
                # 스택에 파이프 있으면
                if pipe:
                    # 순회하면서 파이프 두동강내기
                    for j in range(len(pipe)):
                        pipe[j] += 1
                    # print('cutting pipe', pipe)
            # 괄호가 열렸는데 바로 옆에 안닫히면
            if token == '(' and razer[i+1] != ')':
                # 파이프 있다는 뜻
                pipe.append(1)
                # print('pipe append', pipe)
        # 닫힌 괄호를 만날 때 이전 토큰을 확인하기 위해서 i-1을 진행
        # out of range 방지용
        if i != 0:
            # 닫힌 괄호를 만났는데 그 전 인덱스에 열린 괄호가 없으면
            if token == ')' and razer[i-1] != '(':
                if pipe:
                    result += pipe.pop()
                # print('output pipe', result)
            else:
                continue
    while pipe:
        result += pipe.pop()
    print(f'#{tc} {result}')

'''
효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 
레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.

쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.

 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.

 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.

 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
'''