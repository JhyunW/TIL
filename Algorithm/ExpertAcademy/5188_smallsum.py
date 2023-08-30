# SW Expert
# 5188_최소합
move_x = [0, 1]  # 오른쪽 아래쪽
move_y = [1, 0]
def search(x, y):
    global start
    global small
    for q in range(2):  # 이동, 해당 위치의 숫자 더하기
        if x < N and y < N and data[x][y] == 0:  # 현재의 좌표가 N * N 을 벗어나지 않고, 방문기록이 없을경우
            start += arr[x][y]  # 그 지점의 숫자 더하기
            if start >= small:  # 만약 진행 도중 현재의 가장 작은 수보다 크거나 같아지면 반복할 필요없이 for문 나오기
                break
            data[x][y] = 1  # 현재 값이 최저 값보다 작은동안은 이동한 길 좌표 찍으며 진행
            if x == N-1 and y == N-1:  # 오른쪽 끝 지점에 도달 했을 시
                if small > start:  # 현재의 최소와 비교했을시 더 작으면
                    small = start  # 최소 숫자 할당
                    break  # continue 도 가능
        if x + move_x[q] < N and y + move_y[q] < N:  # 현재 지점을 더한 후 다음 행열이 범위를 벗어나지 않을때 이동
            search(x + move_x[q], y + move_y[q])  # 다음 행열 함수 불러오기

    data[x][y] = 0  # 반복문 마지막에 데이터 현재좌표 0으로 초기화
    start -= arr[x][y]  # 현재 좌표 값을 빼주고 전 좌표로 이동

T = int(input())  # 테스트케이스

for tc in range(1, T+1):
    N = int(input())  # N * N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]  # N 줄에 걸쳐 입력
    data = [[0] * N for _ in range(N)]
    start = 0  # 시작지점 숫자 저장
    small = 999999  # 숫자를 저장할 공간
    search(0, 0)  # 왼쪽 끝 부터 시작
    print(f'#{tc} {small}')