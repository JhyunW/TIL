# SW Expert
# 4828_ min max

T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N = int(input()) # 양수의 갯수
    ai = list(map(int, input().split())) # 양수 입력

    big_num = max(ai)
    min_num = min(ai)
    # big_num = 0
    # small_num = ai[0]
    # for q in ai:
    #     if big_num < q:
    #         big_num = q
    #     if small_num > q:
    #         small_num = q

    print(f'#{tc} {big_num - min_num}')