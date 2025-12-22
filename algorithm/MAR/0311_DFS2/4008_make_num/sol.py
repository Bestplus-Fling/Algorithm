import sys
sys.stdin = open('input.txt', 'r')
#####################################


# 계산용
def check(n, prv, nxt):
    if n == 0:
        return prv+nxt
    elif n == 1:
        return prv-nxt
    elif n == 2:
        return prv*nxt
    else:
        return int(prv/nxt)


# 순열(인데 왜 함수명은 조합이냐 물으신다면 저도 모릅니다)
def comb(idx, op):
    global min_num, max_num
    # 연산 끝나면 최대, 최소 갱신
    if idx == N-1:
        min_num = min(min_num, op)
        max_num = max(max_num, op)
        return
    # 연산자 리스트를 순회, 선택할 때와 선택하지 않을 때를 확인한다.
    for i in range(4):
        if not operator_list[i]:
            continue
        # 연산자를 선택했다면, 연산자를 사용했다는 흔적을 남긴다.
        operator_list[i] -= 1
        # 함수 호출 전 연산을 마친다.
        temp = check(i, op, num_list[idx+1])
        # 연산된 내용을 가지고 재귀함수 호출
        comb(idx+1, temp)
        # 다시 돌아왔다면, 원상복구
        operator_list[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operator_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_num, min_num = -float('inf'), float('inf')
    comb(0, num_list[0])
    print(f'#{tc}', max_num - min_num)
