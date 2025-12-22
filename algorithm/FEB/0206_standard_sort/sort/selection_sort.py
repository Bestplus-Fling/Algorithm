def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i #인덱스로 저장(위치를 교환하기 위해서)
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:   # 현재까지의 최값보다 작은 값이 발견될 경우
                min_idx = j     # 최소값 인덱스를 갱신

        # 끝까지 돌아서 최소값을 찾았으면, i와 교환해서 최소값을 앞으로 이동한다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 10, 22, 11]
selection_sort(arr)
print(arr)