T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = sorted(list(map(int, input().strip())))
    # 참 거짓 출력
    t = "true"
    f = "false"
    # 초기 상태 = False
    is_true = False
    for i in range(1, 5):
        if (n[i - 1] == n[i] == n[i + 1]) or (n[i - 1] + 1 == n[i] == n[i + 1] - 1):
            is_true = True
            break
        # 해야 하는 것 : ex)123123일때 정렬하면 112233으로 바뀌는데 어떻게 해결할 것인가
    if is_true:
        print(f"#{tc} {t}")

    else:
        print(f"#{tc} {f}")
