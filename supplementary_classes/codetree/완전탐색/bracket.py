A = input()

# 완전탐색
# 4개의 문자를 선택하여
# (()) 인지 확인
# => 100 C 4
ans = 0
for i1 in range(len(A)):
    for i2 in range(i1+1, len(A)):
        for i3 in range(i2+1, len(A)):
            for i4 in range(i3+1, len(A)):
                # 현재 4개의 문자를 선택한 상태이다.
                # 이때, 4개의 문자가 (()) 인지 확인해서 맞다면 counting
                if i1 + 1 == i2 and i3 + 1 == i4:
                    if A[i1] == '(' and A[i2] == '(' and A[i3] == ')' and A[i4] == ')':
                        ans += 1

print(ans)


# for i1 in range(len(A)):
#     i2 = i1 + 1
#     for i3 in range(i2+1, len(A)-1):
#         i4 = i3 + 1
#         # 현재 4개의 문자를 선택한 상태이다.
#         # 이때, 4개의 문자가 (()) 인지 확인해서 맞다면 counting
#         if A[i1] == '(' and A[i2] == '(' and A[i3] == ')' and A[i4] == ')':
#             cnt += 1
# print(cnt)