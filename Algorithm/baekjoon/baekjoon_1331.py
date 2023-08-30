# baekjoon
# 1331_나이트 투어
move_x = ['6', '5', '4', '3', '2', '1']
move_y = ['A', 'B', 'C', 'D', 'E', 'F']

# 나이트의 이동 가능 범위
k_x = [-2, -1, 1, 2, 2, 1, -1, -2]  # 왼쪽 위부터 반시계
k_y = [-1, -2, -2, -1, 1, 2, 2, 1]
knight = []
for i in range(36):
    knight.append(input())  # 나이트의 좌표 순서

for q in range(len(knight)):  # 나이트의 체스판 좌표를 배열 좌표로 그대로 옮기기
    for q1 in range(6):
        if knight[q][0] == move_y[q1]:
            knight[q] = [(int(knight[q][1]) - 6) * -1, q1]  # x와 y좌표
            break  # 좌표를 찾고 다음 좌표 탐색
start = knight[0]  # 나중에 돌아올때를 위한 시작 지점 체크
data = [knight[0]]  # 방문 기록 체크
now = knight[0]  # 지금의 나이트 위치 표시
result = 'Valid'
for w in range(1, 36):
    safe = 0
    for e in range(8):
        if knight[w] not in data and [now[0]+k_x[e], now[1]+k_y[e]] == knight[w]:  # 맞는 경로에 있을시
            safe = 1
            now = knight[w]
            data.append(knight[w])
            break
    if safe == 0:  # 만약 맞는 위치에 없을 시
        result = 'Invalid'
        break
if result == 'Valid':
    for e in range(8):
        if [now[0]+k_x[e], now[1]+k_y[e]] != start:
            result = 'Invalid'
        else:
            result = 'Valid'
            break
print(result)

