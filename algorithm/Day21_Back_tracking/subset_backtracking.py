def find_subsets(start, current_subset, acc):
    global cnt
    cnt += 1
    if acc > target_sum:
        return
    if acc == target_sum:
        print(current_subset)
    for i in range(start, len(nums)):

        num = nums[i]
        current_subset.append(num)
        find_subsets(i+1, current_subset, acc + num)
        current_subset.pop()


nums = list(range(1, 11))
target_sum = 10
cnt = 0
result = []
find_subsets(start=0, current_subset=[], acc=0)
print(cnt)