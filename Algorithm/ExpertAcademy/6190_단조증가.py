# SW Expert
# 6190_정곤이의 단조 증가하는 수

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 숫자 입력
    arr = list(map(int, input().split()))  # 곱할 숫자들
    best = 0  # 최고 크기

    go = 0  # 최고 숫자에 넣을지 말지

    for i in range(N-1):  # 끝의 바로 전까지 조사
        now = arr[i] * arr[i+1]  # 현재 지점과 지점의 앞부분 숫자 곱
        now_str = str(now)  # 길이를 알기위해 스트링으로 변환
        if len(now_str) > 1:  # 만약 길이가 1보다 길면
            for q in range(len(now_str) - 1):  # 최대 길이의 바로 전까지 조사
                if int(now_str[q]) > int(now_str[q+1]):  # 만약 뒤의 숫자가 더 작으면
                    go = 1  # 출력안해도된다고 표시
                    break  # 포문 탈출
            if go == 0 and len(set(now_str)) > 1:
                if best < now:
                    best = now
            elif go == 1:
                go = 0

    if best == 0:
        best = -1

    print(f'#{tc} {best}')
