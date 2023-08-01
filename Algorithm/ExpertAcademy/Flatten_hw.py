# SW Expect 1208_Flatten
tc = 10

for test in range(tc):
    dump = int(input()) # 덤프 횟수
    box = list(map(int, input().split())) # 박스 높이
    gap = 0 # 숫자 차이
    for move in range(dump): # 흙(박스) 를 옮길 횟수 한번에 하나씩 가능
        high = 0 # 가장 높은 값을 저장한 변수
        high_index_num = 0 # 가장 높은 값을 가진 인덱스 번호를 저장할 변수
        low = box[0] + 1 # 가장 낮은 높이를 저장할 변수
        low_index_num = 0 # 가장 낮은 높이를 가진 인덱스 번호 저장
        for comparison in range(len(box)): # 흙(박스)의 높이를 하나하나 비교해서 가장 높은것과 낮은것을 골라냄
            if high < box[comparison]:
                high = box[comparison]
                high_index_num = comparison

            if low > box[comparison]:
                low = box[comparison]
                low_index_num = comparison

        if low == high: # 만약 옮길것이 더이상 없다면 0을 반환후 반복문 종료
            print(f'#{test + 1} 0')
            break

        box[high_index_num] -= 1 # 가장 높은값은 -1
        box[low_index_num] += 1 # 가장 낮은 값은 +1

        # 가장 헤맨구간 함수들을 한번 더 초기화 해 줘야함 안그럼 원하는 답이 안나옴
        high = 0
        high_index_num = 0
        low = box[0] + 1
        low_index_num = 0

        for comparison_2 in range(len(box)): # 옮기고 난 후의 가장 높은값과 낮은값의 차 구하는 과정
            if high < box[comparison_2]:
                high = box[comparison_2]
                high_index_num = comparison_2

            if low > box[comparison_2]:
                low = box[comparison_2]
                low_index_num = comparison_2

        gap = box[high_index_num] - box[low_index_num]
    print(f'#{test + 1} {gap}')

