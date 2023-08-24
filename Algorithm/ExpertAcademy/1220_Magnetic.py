# SW Expert
# 1220_Magnetic

# 위( N극 2번이 끌려옴
# 아래( S극 1번이 끌려옴

for tc in range(1, 11):
    long = int(input())

    arr = []
    for i in range(long):
        arr.append(list(map(int, input().split())))
    print(arr)
    count = 0



    for q in range(100):
        N_count = 0
        S_count = 0
        for q1 in range(100):
            if arr[q1][q] == 1 and N_count == S_count:  # 세로줄 탐색
                N_count += 1
            elif arr[q1][q] == 2 and N_count > S_count:
                S_count += 1

        count += S_count

    print(f'#{tc} {count}')

