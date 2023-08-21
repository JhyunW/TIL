
T = int(input())  # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N장의 카드, M번째 순서 입력
    arr = list(map(str, input().split()))  # N장의 카드 각각의 숫자 또는 기호 입력
    card_B = []  # 홀수 카드만
    card_C = []  # 짝수 카드만

    bonus = 0  # +가 나오면 더할 보너스 카드

    while arr:
        a = arr.pop(0)  # 맨 앞의 숫자부터 꺼내야 하므로

        if a == '+':  # + 가 나온경우
            bonus += 1

        else:
            b = int(a) + bonus  # 아닐경우 숫자이므로 보너스 숫자와 더한 후
            if b % 2 != 0:  # 홀수일 경우
                card_B.append(b)
            else:  # 짝수일 경우
                card_C.append(b)

    ssafy = 0  # 김싸피의 점수

    if len(card_C) < M:  # C 덱에서 M 번째에 뽑을 카드가 없다면
        ssafy += 0  # 0점 휙득
    else:
        ssafy += card_C[-M]  # 뒤에서부터 카드를 빼므로 len(card_C) - M - 1

    if len(card_B) < M:  # B 덱에서 M 번째에 뽑을 카드가 없다면
        ssafy += 0
    else:
        ssafy += card_B[M - 1]  # M-1 번째 인덱스의 값 더하기

    print(f'#{tc} {ssafy}')