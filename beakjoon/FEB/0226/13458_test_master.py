# N개의 시험장
# 각각의 시험장마다 응시자들이 있다. 응사자의 수는 Ai명
# 감독관은 총감독관과 부감독관 두 종류
# B : 총감독관이 한 시험장에서 감시할 수 있는 응시자의 수
# C : 부감독관이 감시할 수 있는 응시자의 수
# 각각 시험장에 총 감독관은 오직 1명만, 부감독관은 여러 명 있어도 된다.

# N : 시험장 수
N = int(input())
# arr : 시험장 당 응시자 수
arr = list(map(int, input().split()))
# B, C : 총, 부 감독관이 감시할 수 있는 응시자 수
B, C = map(int, input().split())
count = 0


# 방법 2 총감독관 제외, 부감독관이 감시할 수 있는 인원으로 응시자를 나눌 때의 몫 + 1
for i in range(N):
    temp = arr[i] - B
    count += 1
    if temp > 0:
        count += (temp // C) + (1 if temp % C > 0 else 0)
print(count)

# 방법 1 총감독관을 제외한 부감독관 수를 확인(시간 초과)
# for i in range(N):
#     temp = arr[i] - B
#     count += 1
#     while temp > 0:
#         temp -= C
#         count += 1
# print(count)
