import math

# 예제 1
hallcup = (254, 127)    # 홀컵 좌표
my_ball = (224, 97)     # 현재 공 좌표
target = (244, 110)     # 목적구 좌표

# 예제 2
# hallcup = (0, 0)    # 홀컵 좌표
# my_ball = (127, 63.5)     # 현재 공 좌표
# target = (15.8, 30)     # 목적구 좌표
R = 5.73                # 공의 지름


a = math.dist(hallcup, my_ball) # 현재 공에서 홀까지 거리
c = math.dist(hallcup, target)  # 목적구부터 홀까지의 거리
c = math.dist(target, my_ball)  # 현재 공과 목적구의 거리
print(f"현재 공에서 홀컵까지의 거리 a: {a}, \n목적구부터 홀컵까지의 거리 b: {c}, \n현재 공부터 목적구의 거리 c: {c}")

# 각도 '가'를 찾기 위한 밑변, 높이 계산
x = hallcup[0] - my_ball[0]
y = hallcup[1] - my_ball[1]
print(f"밑변 : {y}, 높이 : {x}")

# 각도 '가' 계산(atan2 메서드 사용)
angle_a = abs(math.degrees(math.atan2(x, y)) - 90)
print(f"각도 '가' : {angle_a}")

# cos 법칙을 사용하여 각도 '다'를 찾아 변수에 저장
angle_c = math.acos(((a**2) + (c ** 2) - (c ** 2)) / (2 * a * c))
print(f"각도 '다': {math.degrees(angle_c)}")

# 변 d를 구하는 변수 - cos 공식 이용(각도 다, 변 a, 변 R+b)
d = math.sqrt((a**2) + ((c + R) ** 2) - (2 * a * (c + R) * math.cos(angle_c)))
print("변 d :", d)

# cos 법칙을 이용해 각도 '나'를 찾는다.
angle_b = (math.degrees(math.acos(((a**2) + (d**2) - ((R + c) ** 2)) / (2 * a * d))))
print("각도 '나':", angle_b)

# 최종적으로 나아가는 방향을 찾는 변수
direction_target = angle_a+angle_b
print("빗각 :", direction_target)