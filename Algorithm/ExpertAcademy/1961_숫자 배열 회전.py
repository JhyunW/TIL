# SW Expert
# 1961_숫자 배열 회전

T = int(input())  # 테케

for tc in range(1, T+1):
    N = int(input())  # 행열

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    print(f'#{tc}')

    # 90도 회전
    one = [[]for _ in range(N)]
    for q in range(N):  # y축
        for q1 in range(-1, -N-1, -1):  # x축
            one[q].append(arr[q1][q])

    # 180도 회전
    two = [[]for _ in range(N)]
    count = 0
    for w in range(-1, -N-1, -1):
        for w1 in range(-1, -N-1, -1):
            two[count].append(arr[w][w1])
        count += 1

    # 270도 회전
    three = [[]for _ in range(N)]
    count = 0
    for e in range(-1, -N-1, -1):
        for e1 in range(N):
            three[count].append(arr[e1][e])
        count += 1

    for r in range(N):
        for p_one in range(N):
            print(one[r][p_one], end = '')
        print(' ', end = '')

        for p_two in range(N):
            print(two[r][p_two], end = '')
        print(' ', end='')

        for p_three in range(N):
            print(three[r][p_three], end='')
        print()