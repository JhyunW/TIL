# Baekjoon
# 1063_킹
# 나는 체스판을 뒤집을 생각이므로 위쪽은 아래로 아래쪽은 위로 이동
# x열 8 -> 1순 y열 a -> b 순

arr = [[0]*8 for _ in range(8)]  # 8*8 배열 생성
K, R, N = map(str, input().split())  # 문자열로 킹 돌 움직이는 횟수 받기
move = []
for _ in range(int(N)):  # 움직임 명령어 입력
    move.append(input())
move_x = [-1, -1, 0, 1, 1, 1, 0, -1]  # 위 왼위 왼 아왼 아 ~~
move_y = [0, -1, -1, -1, 0, 1, 1, 1]
ar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 0~7 까지의 알파벳
for i in range(8):  # 킹과 돌의 x좌표 구하기
    if ar[i] in K:
        k_y = i
    if ar[i] in R:
        r_y = i

k_x = int(K[1]) - 1  # 킹과 돌의 y좌표
r_x = int(R[1]) - 1

for q in move:
    if q == 'B':
        mx_k, my_k = k_x + move_x[0], k_y + move_y[0]  # 왕의 이동
        mx_r, my_r = r_x + move_x[0], r_y + move_y[0]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k
        # 한칸위로
    elif q == 'LB':
        # 위쪽 왼
        mx_k, my_k = k_x + move_x[1], k_y + move_y[1]  # 왕의 이동
        mx_r, my_r = r_x + move_x[1], r_y + move_y[1]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k
    elif q == 'L':
        # 한칸 왼쪽
        mx_k, my_k = k_x + move_x[2], k_y + move_y[2]  # 왕의 이동
        mx_r, my_r = r_x + move_x[2], r_y + move_y[2]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k
    elif q == 'LT':
        # 아래 왼
        mx_k, my_k = k_x + move_x[3], k_y + move_y[3]  # 왕의 이동
        mx_r, my_r = r_x + move_x[3], r_y + move_y[3]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k
    elif q == 'T':
        # 한칸 아래
        mx_k, my_k = k_x + move_x[4], k_y + move_y[4]  # 왕의 이동
        mx_r, my_r = r_x + move_x[4], r_y + move_y[4]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k
    elif q == 'RT':
        # 아래 오
        mx_k, my_k = k_x + move_x[5], k_y + move_y[5]  # 왕의 이동
        mx_r, my_r = r_x + move_x[5], r_y + move_y[5]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k
    elif q == 'R':
        # 한칸 오른쪽
        mx_k, my_k = k_x + move_x[6], k_y + move_y[6]  # 왕의 이동
        mx_r, my_r = r_x + move_x[6], r_y + move_y[6]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k
    elif q == 'RB':
        # 오른쪽 위
        mx_k, my_k = k_x + move_x[7], k_y + move_y[7]  # 왕의 이동
        mx_r, my_r = r_x + move_x[7], r_y + move_y[7]  # 돌의 이동
        if 0 <= mx_k < 8 and 0 <= my_k < 8 and [mx_k, my_k] == [r_x, r_y]:  # 킹이 배열을 안벗어나고 돌이랑 겹칠때
            if 0 <= mx_r < 8 and 0 <= my_r < 8:  # 돌의 이동에도 배열 밖으로 안나갈때
                k_x, k_y, r_x, r_y = mx_k, my_k, mx_r, my_r  # 왕과 돌 좌표 이동
        elif 0 <= mx_k < 8 and 0 <= my_k < 8:  # 돌이 없을경우 킹만 이동
            k_x, k_y = mx_k, my_k

result_k = ar[k_y] + str(k_x + 1)
result_r = ar[r_y] + str(r_x + 1)

print(result_k)
print(result_r)