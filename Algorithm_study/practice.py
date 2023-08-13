# 숫자 카드

# 0~9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
# 카드 장수가 같을때는 적힌 숫자가 큰 쪽을 출력


T = int(input())  # 테스트 케이스
move_x = [-1, 0, 1, 0]  # 위 왼 아 오
move_y = [0, -1, 0, 1]
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[] for _ in range(N)]  # N줄

    for i in range(N):
        arr[i] = list(map(int, input().split()))
    

    best = 0

    for x in range(N):
        for y in range(M):
            plus = arr[x][y]
            for move in range(4):
                for q in range(1, arr[x][y]+1):
                    xx, yy = x + (move_x[move] * q), y + (move_y[move] * q)
                    if 0 <= xx < N and 0 <= yy < M:
                        plus += arr[xx][yy]
            
            if best < plus:
                best = plus
    
    print(f'#{tc} {best}')

