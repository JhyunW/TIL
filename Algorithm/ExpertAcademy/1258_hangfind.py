import sys
sys.stdin = open('input.txt')
# SW Expert
# 1258_행렬찾기

def s(x):
    return (x[0] * x[1], x[0])

T = int(input())  # 테케입력

for tc in range(1, T+1):  # 테케반복
    N = int(input())  # 배열 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # N줄의 배열 입력
    check = [[0]*N for _ in range(N)]  # 체크할 N*N 배열 생성
    result = []
    for q in range(N):
        for q1 in range(N):
            if arr[q][q1] != 0 and check[q][q1] == 0:  # 배열에서 0이 아니며, 체크가 안된 지점
                x = q  # 조사좌표
                y = q1  # 조사좌표
                x_len = 1  # x의 길이
                y_len = 0  # y의 길이
                while arr[x][q1] != 0:  # 배열을 벗어나지 않고 지점이 0이 아닐때까지
                    if arr[x][y] != 0:  # 가로줄 끝까지 갔을때
                        check[x][y] = 1  # 체크 지도에도 사용했다고 표기
                        y += 1  # 좌표 한칸 이동
                        if x_len == 1:  # 한칸 밑으로 내려가기 전까진
                            y_len += 1  # y길이 카운트 1
                        if y == N or arr[x][y] == 0:  # 범위를 벗어나거나 0을 만날경우
                            y = q1  # 가로 좌표 돌아오기
                            x += 1  # 한칸 밑으로 내려가기
                            if arr[x][y] != 0:
                                x_len += 1  # x의 길이 더하기
                result.append([x_len, y_len])

    number = len(result)  # 상자의 갯수
    result.sort(key = s)


    print(number, end = ' ')
    for i in range(len(result)):
        print(*result[i], end = ' ')
    print()

