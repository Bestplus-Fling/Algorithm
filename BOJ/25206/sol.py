import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/25206
# 작성 코드 시작

grade_table = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

credit = 0
gpa = 0
for i in range(20):
    sub, c, g = input().split()
    if g == "P":
        continue
    c_int = int(float(c))
    credit += c_int
    gpa += c_int * grade_table[g]
print(gpa / credit)