import math
# 내공 1,1
# 넣을 공 5.2
# 홀 6.2

ball_my = (1, 1)
ball_com = (5, 2)
hall = (6, 4)


a = abs(ball_my[0] - hall[0])
b = abs(ball_my[1] - hall[1])

r = math.sqrt(a**2 + b**2)  # 빗변의 길이
tan = math.atan(b/a)  # 탄젠트 밑변 / 높이
# 홀과 내공 기준으로 잡은 방향 각
way_1 = math.degrees(tan)  # 각도로 변환


# 컴퓨터 공 기준 각 구해보기
a_1 = abs(ball_com[0] - hall[0])
b_1 = abs(ball_com[1] - hall[1])

r = math.sqrt(a_1 ** 2 + b_1 ** 2)  # 넣어야 하는 공과 홀을 이었을때의 각도
