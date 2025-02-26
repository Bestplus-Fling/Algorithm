# 백설공주는 의자 일곱개, 접시 일곱개, 나이프 일곱개를 준비
# 갑자기 9명이 돌어와버렸다.(미친놈들인가)
# 난쟁이가 쓰고 다니는 모자에 100보다 작은 양의 정수를 적어 놓았다
# 일곱 난쟁이의 모자에 쓰여 있는 숫자의 합이 100이 되도록 적어 놓았다.
# 완전탐색


def search_hnd(idx=0, num=[], cnt=0):
    if idx == 9 and cnt != 7:
        return
    if cnt == 7:
        if sum(num) != 100:
            return
        for i in range(7):
            result.append(num[i])
        return

    num.append(arr[idx])
    search_hnd(idx + 1, num, cnt + 1)
    if result:
        return
    num.pop()
    search_hnd(idx + 1, num, cnt)
    if result:
        return


arr = [int(input()) for _ in range(9)]
result = []
search_hnd()
for i in range(7):
    print(result[i])
