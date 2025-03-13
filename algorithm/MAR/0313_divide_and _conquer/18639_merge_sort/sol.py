import sys
sys.stdin = open('input.txt', 'r')
#####################################


def divide(dl):
    global ans
    # 좌우 분할값이 1일 때 반환 후 merge 실행
    n = len(dl)
    if n == 1:
        return dl

    # 반환값들로 merge 실행
    l_dl = divide(dl[:n//2])
    r_dl = divide(dl[n//2:])
    if l_dl[-1] > r_dl[-1]:
        ans += 1
    return merge(l_dl, r_dl)


def merge(l_list, r_list):
    lm, rm = len(l_list), len(r_list)
    m_list = []
    l, r = 0, 0
    while l < lm and r < rm:
        if l_list[l] < r_list[r]:
            m_list.append(l_list[l])
            l += 1
        else:
            m_list.append(r_list[r])
            r += 1
    while l < lm:
        m_list.append(l_list[l])
        l += 1
    while r < rm:
        m_list.append(r_list[r])
        r += 1
    return m_list


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    # 분할 방법: [:N//2], [N//2:]
    al = divide(arr)
    print(f'#{tc}', al[N//2], ans)

