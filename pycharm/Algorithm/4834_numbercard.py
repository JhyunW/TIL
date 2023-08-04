tc = int(input())

for test in range(tc):
    card = int(input()) # 카드 몇장인지 입력
    ai = list(map(int, input())) # 카드 넘버 입력
    print(ai)
    counting_arr = [0] * 10 # 넘버 카운딩 배열
    print(counting_arr)

    for num in ai:
        counting_arr[num] += 1

    print(counting_arr)
    result = 0
    num = 0
    for index in range(len(counting_arr)):
        if counting_arr[index] >= result:
            result = counting_arr[index]
            num = index

    print(f'#{tc+1} {num} {result}')