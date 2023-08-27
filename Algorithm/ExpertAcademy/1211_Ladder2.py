import sys, copy
sys.stdin = open('input.txt')

# SW Expert
# 1211_Ladder2

move_x = [0, 0, 1]  # 왼 오 아
move_y = [-1, 1, 0]

for t in range(10):
    tc = int(input())  # 테케 입력

    arr = [0] * 100
    for i in range(100):
        arr[i] = list(map(int, input().split()))

        short = 10000  # 최소거리
        result = 0  # 짧은 시작점
    for q in range(100):  # 맨 윗줄 끝까지 탐색
        start = 0  # 시작 x좌표
        count = 0  # 몇칸 이동하는지
        if arr[start][q] == 1:  # 1인 지점부터 시작
            check = copy.deepcopy(arr)
            now = q
            while start != 99:
                for move in range(3):
                    mx, my = start + move_x[move], now + move_y[move]
                    if 0 <= mx < 100 and 0 <= my < 100 and check[mx][my] == 1:
                        check[start][now] = 9  # 지나간곳은 9로 체크
                        start, now = mx, my  # 한칸 앞으로 이동
                        count += 1  # 이동할때마다 카운트 올리기
                        break
            
            if short > count:  # 최단거리보다 더 짧은경우
                short = count  # 짧은거리 교체
                result = q  # 시작점 기록
    
    print(f'#{tc} {result}')