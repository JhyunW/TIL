import sys
sys.stdin = open('input.txt')

# SW Expert
# 12712_파리퇴치

move_x = [-1, 0, 1, 0, -1, 1, 1, -1]  # 위 왼 아 오
move_y = [0, -1, 0, 1, -1, -1, 1, 1]  # 대각선 왼왼오오

T = int(input())  # 테케 입력
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 배열, 범위

    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 입력

    result = 0  # 최대 파리퇴치수

    for q in range(N):
        for q1 in range(N):  # 배열 순회 반복문
            best = 0
            count_1 = arr[q][q1]
            count_2 = arr[q][q1]
            for w in range(1, M):  # 스프레이 범위 반복문
                for move in range(8):  # 십자가 범위
                    mx, my = q + move_x[move] * w, q1 + move_y[move] * w  # 상하좌우/왼왼오오
                    if 0 <= mx < N and 0 <= my < N:
                        if move < 4:
                            count_1 += arr[mx][my]  # 조건에 충족한 + 배열 숫자 더하기
                        else:
                            count_2 += arr[mx][my]  # X자 더하기

            if count_1 >= count_2:  # x와+ 비교
                best = count_1
            else:
                best = count_2

            if best > result:  # 둘중 가장 큰 값과 최고 숫자 비교
                result = best

    print(f'#{tc} {result}')