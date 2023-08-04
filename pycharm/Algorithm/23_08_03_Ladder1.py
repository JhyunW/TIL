# SW Expert Ladder1
import sys

sys.stdin = open('input.txt')

t = 10  # 테스트 케이스

for tc in range(t):

    arr = [[0] * 100 for _ in range(100)]  # 100 * 100 리스트 생성

    test = int(input())  # 테스트 넘버 입력

    for z in range(100):  # 100개씩 100줄 입력
        arr[z] = list(map(int, input().split()))

    x_point = 0  # 도착점 arr[99][x]
    for x in range(100):
        if arr[99][x] == 2:
            x_point = x
            break
    y_point = 99
    # --------------------------- 사다리 이동 로직--------------------------
    # 이동할때 지금 있는 자리에 숫자 9로 바꾼 후 이동함으로써 되돌아가는일 방지.

    while y_point >= 0: # y_point 가 맨 위에 도착할때까지 진행
        if x_point == 99:  # 제일 오른쪽일때는 왼쪽과 직진만 비교 - 인덱스 오류가 안뜨기 위함
            if arr[y_point][x_point - 1] == 1:
                arr[y_point][x_point] = 9
                x_point -= 1
            else:
                y_point -= 1

        elif x_point == 0:# 제일 왼쪽일때는 오른쪽과 직진만 비교 - 인덱스 오류 방지 위함
            if arr[y_point][x_point + 1] == 1:
                arr[y_point][x_point] = 9
                x_point += 1
            else:
                y_point -= 1

        else: # 맨 왼쪽, 오른쪽이 아닐시에 좌, 우, 위 순서로 비교
            if arr[y_point][x_point - 1] == 1:
                arr[y_point][x_point] = 9
                x_point -= 1

            elif arr[y_point][x_point + 1] == 1:
                arr[y_point][x_point] = 9
                x_point += 1

            else:
                arr[y_point][x_point] = 9
                y_point -= 1

    print(f'#{test} {x_point}')
    # for tr in arr:
    #     print(tr)
