import sys
sys.stdin = open('input.txt')

# SW Expert
# 1210_Ladder1

move_x = [0, 0, -1]  # 왼 오 위 순으로 비교(좌우 먼저 길이 있는지 탐색을 위함.)
move_y = [-1, 1, 0]

for t in range(1, 11):
    tc = int(input())  # 테케 번호
    arr = [0] * 100
    for i in range(100):  # 배열 생성
        arr[i] = list(map(int, input().split()))
    
    # print(arr)

    now_x = 99  # 골인 지점
    now_y = 0
    for q in range(100):  # 골인지점 찾는 반복문
      if arr[99][q] == 2:
          now_y = q
          break
    

    while now_x != 0:  # 현재의 위치가 맨 위에 도달할시에 와일문 종료
        # print(now_x, now_y)
        for move in range(3):  # 왼 오 위 비교
            mx, my = now_x + move_x[move], now_y + move_y[move]
            #  배열을 벗어나지 않으며 길목 1 로 표시되었을때
            if 0 <= mx < 100 and 0 <= my < 100 and arr[mx][my] == 1:
                arr[now_x][now_y] = 9  # 지나온 길 표기
                now_x, now_y = mx, my  # 해당 길로 이동
                break  # 포문 종료
    
    print(f'#{tc} {now_y}')