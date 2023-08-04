# SW Expert 기차 사이 파리
# 정수를 소수점 밑 6자리까지 출력하기
t = int(input())

for tc in range(1, t + 1):
    D, A, B, F = map(int, input().split())
    # 사이거리, 기차A속도, 기차B속도, 파리F속도
    move = 0

    while D > 1:
        D_minus = A + B
        if D - D_minus < 0:
            last_dance = D / (A + B)
            move += F * last_dance
            D = 0

        else:
            D -= D_minus
            move += F

    print(f'# {tc} {round(float(move),6)}')
