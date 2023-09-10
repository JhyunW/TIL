import math
# 내공 1,1
# 넣을 공 5.2
# 홀 6.2

ball_my = (150, 80)
ball_com = (171, 91)
hall = (254, 127)


a = abs(ball_my[0] - hall[0])  # x
b = abs(ball_my[1] - hall[1])  # y

r_1 = math.sqrt(a**2 + b**2)  # 빗변의 길이
tan = math.atan(a/b)  # 탄젠트 밑변 / 높이
# 홀과 내공 기준으로 잡은 방향 각
way_1 = math.degrees(tan)  # 각도로 변환 가의 각도


# 컴퓨터 공 기준 각 구해보기
a_1 = abs(ball_com[0] - hall[0])  # 밑변
b_1 = abs(ball_com[1] - hall[1])  # 높이

r_2 = math.sqrt(a_1 ** 2 + b_1 ** 2)  # 넣어야 하는 공과 홀을 이었을때의 b의 길이
tan_2 = math.atan(a_1/b_1)  # 가 - 이거의 결과값
way_da = way_1 - math.degrees(tan_2)  # 다 의 각도

d = math.sqrt(r_1**2 + (r_2+5.73)**2 - 2*r_1 * (r_2 + 5.73) * math.cos(way_da))
d_re = (r_2 + 5.73) * math.sin(way_da)  # (b + 2r) * (sin_da)
way_na = math.asin(d_re / d)
print(way_na)
way_na_de = math.degrees(way_na)
print(way_na_de + way_1)
