tc = 1

for test in range(tc):
    dump = int(input()) # 덤프 횟수
    box = list(map(int, input().split())) # 박스 높이
    gap = 0 # 숫자 차이
    for move in range(dump):
        high = 0
        high_index_num = 0
        low = box[0] + 1
        low_index_num = 0
        for comparison in range(len(box)):
            if high < box[comparison]:
                high = box[comparison]
                high_index_num = comparison

            if low > box[comparison]:
                low = box[comparison]
                low_index_num = comparison

        if low == high:
            print(f'#{test + 1} 0')
            break

        box[high_index_num] -= 1
        box[low_index_num] += 1

        for comparison in range(len(box)):
            if high < box[comparison]:
                high = box[comparison]
                high_index_num = comparison

            if low > box[comparison]:
                low = box[comparison]
                low_index_num = comparison

        gap = box[high_index_num] - box[low_index_num]
    print(gap)

