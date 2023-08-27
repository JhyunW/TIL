import sys
sys.stdin=open('input.txt')
# SW Expert
# 1216_회문2

for t in range(1, 11):
    tc = int(input())  # 테스트 케이스 번호
    arr_x = []  # 정식배열
    arr_y = []
    for i in range(100):  # x배열
        arr_x.append(input())  # 리시트 글자추가
    for i1 in range(100):
        trash = ''
        for i2 in range(100):  # 회전배열
            trash += arr_x[i2][i1]
        arr_y.append(trash)
    start = 0  # 비교 시작지점
    end = 2  # 비교 끝 지점

    for q in range(100):  # 100줄 반복
        move = 0  # 한칸씩 비교 범위를 늘려감
        while start + end < 100:  # 최고 기록 + 움직인 거리 가 리스트를 벗어나지 않을때까지
            a = arr_x[q][start:end+move+start]  # q번째 줄에서 start~ 최고+이동
            b = arr_y[q][start:end+move+start]
            if a == a[::-1] or b == b[::-1]:  # 배열 열을 뒤집어도 똑같을때
                # print(q,start, end, move)
                end = end + move  # 비교 문자의 길이 저장
                move += 1  # 최고 길이의 한칸 앞부터 다시 계산

            else:
                move += 1
            if end + move == 100 and start + end < 100:
                start += 1
                move = 0
        
        start = 0  # 한 줄이 끝났으므로 시작 지점 초기화


    print(f'#{tc} {end}')

