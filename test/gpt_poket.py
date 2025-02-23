import math

# 예제 1 (우측 상단)
# hallcup = (254, 127)    # 홀컵 좌표 (Hole)
# my_ball = (224, 97)     # 현재 공 좌표 (my ball)
# target = (244, 110)     # 목적구 좌표 (target)

# 예제 2 (좌측 하단)
# hallcup = (0, 0)    # 홀컵 좌표
# my_ball = (127, 63.5)     # 현재 공 좌표
# target = (15.8, 30)     # 목적구 좌표

# 예제 3 (중앙 상단)
# hallcup = (127, 127)    # 홀컵 좌표 (Hole)
# my_ball = (127, 30)     # 현재 공 좌표 (my ball)
# target = (127, 100)     # 목적구 좌표 (target)

# 예제 4 (우측 하단)
hallcup = (254, 0)    # 홀컵 좌표 (Hole)
my_ball = (224, 30)     # 현재 공 좌표 (my ball)
target = (204, 50)     # 목적구 좌표 (target)

R = 5.73                # 공의 지름 (볼의 크기)

# ✅ 거리 계산 (math.dist 사용)
a = math.dist(hallcup, my_ball)  # 현재 공에서 홀컵까지 거리
b = math.dist(hallcup, target)   # 목적구부터 홀컵까지의 거리
c = math.dist(target, my_ball)   # 현재 공과 목적구의 거리
print(f"현재 공에서 홀컵까지의 거리 a: {a}, \n목적구부터 홀컵까지의 거리 b: {b}, \n현재 공부터 목적구의 거리 c: {c}")

# ✅ 각도 '가'를 구하기 위한 x, y 차이
x = hallcup[0] - my_ball[0]  
y = hallcup[1] - my_ball[1] 
print(x, y)

# ✅ 각도 '가' 변환 (사진 형태 맞추기: 0° = 위쪽)    
angle_a = (90 - math.degrees(math.atan2(y, x))) 
print(f"각도 '가' (Hole 방향): {angle_a}°")

# 빗변이 0일 경우도 공과 일직선이라는 말(cos 에러 방지)
if angle_a % 90 == 0 or x == 0 or y == 0 or abs(x) == abs(y):
# if False:
    direction_target = angle_a
    
#목적구와 일직선상에 놓여있지 않은 경우 삼각함수를 사용해 빗각을 구한다.
else:
    # ✅ cos 법칙을 사용하여 각도 '다'를 찾음
    cos_c = ((a**2) + (b**2) - (c**2)) / (2 * a * b)
    # cos_c = min(1, max(-1, cos_c))  # acos 오차 방지
    angle_c = math.degrees(math.acos(cos_c))
    print(f"각도 '다' (목적구와 홀 방향): {angle_c}°")

    # ✅ 변 d 계산 (접점을 찾기 위한 거리)
    d = math.sqrt((a**2) + ((b+R) ** 2) - (2 * a * (b+R) * math.cos(math.radians(angle_c))))
    print("변 d (공이 쳐야 할 지점과의 거리):", d)

    # ✅ cos 법칙을 이용해 각도 '나'를 찾음
    cos_b = ((a**2) + (d**2) - ((R + b)**2)) / (2 * a * d)
    # cos_b = min(1, max(-1, cos_b))  # acos 오차 방지
    angle_b = math.degrees(math.acos(cos_b))
    print("각도 '나' (조정 각도):", angle_b)

    # ✅ 최종 방향 변환 (0~360° 범위로 변환)
    direction_target = (angle_a + angle_b) % 360
print(f"🎯 최종 방향 (출력된 형태): {direction_target}°")
