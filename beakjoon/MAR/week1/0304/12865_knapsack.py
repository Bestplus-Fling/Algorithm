def search(idx, value, weight):
    # 종료 조건: K를 초과, idx == N
    global max_value
    if weight > K:
        return
    if idx == N and weight <= K:
        max_value = max(max_value, value)
        return

    search(idx+1, value+value_list[idx], weight+weight_list[idx])

    search(idx + 1, value, weight)


N, K = map(int, input().split())
_list = [tuple(map(int, input().split())) for _ in range(N)]
weight_list, value_list = [], []
max_value = 0
for w, v in _list:
    weight_list.append(w)
    value_list.append(v)
search(0, 0, 0)
print(max_value)