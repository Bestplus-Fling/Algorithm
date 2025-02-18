def count_sort(arr):
    n = len(arr)
    # 각 숫자마다 나오는 개수를 저장하는 배열을 생성

    count_arr = [0] * (max(arr) + 1)
    result = [0] * n

    # 1. 각 요소가 몇번 나왔는지 확인
    for num in arr:
        count_arr[num] += 1
    # 2. 누적합 배열 생성
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # 3. 거꾸로 순회하면서 위치 탐색
    for i in range(n-1, -1, -1):
        val = arr[i]
        # count_arr => 누적합 배열에서 현재 값이 들어가야하는 위치에 저장.
        result[count_arr[val] - 1] = val
        count_arr[val] -= 1

    return result

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print(count_sort(arr))
