def merge_sort(m):
    if len(m) <= 1:  # 만약 리스트의 길이가 하나면
        return m  # m을 반환

    middle = len(m) // 2  # 가운데
    left = m[:middle]  # 왼쪽 오른쪽 for문 생략
    right = m[middle:]
    # for le in range(0, middle):  # 왼쪽
    #     left.append(m[le])
    #
    # for ri in range(middle, len(m)):  # 오른쪽
    #     right.append(m[ri])
    left = merge_sort(left)  # 하나 남을때까지 재귀호출 후 할당.
    right = merge_sort(right)
    # print(left, right)

    left_index, right_index, k = 0, 0, 0
    # 좌, 우 정렬 시도
    while left_index < len(left) and right_index < len(right):
        # 오른쪽이 더 크면
        if left_index < len(left) and right_index < len(right):
        # 원본 배열의 k번째 값인 left 삽입
            m[k] = left[left_index]
            left_index += 1
        
        # 왼쪽이 더 크면
        else:
            # 원복 배열의 k번째에 더 작은 값인 right 삽입
            m[k] = left[left_index]
            left_index += 1
    # 다음 원본 조사 위치로 이동
        k += 1
# 모든 조사 완료후, 아직 남아 있는 값이 있을 수 있다.
    return merge(left, right)

def merge(l,r):
    global ans
    if l[-1] > r[-1]:
        ans += 1
    arr = []
    f_len = len(l) + len(r)  # 반복문을 돌리기 위한 두개의 길이 합
    l_pluse = 0  # l과r의 0번째인덱스부터 세기위한 카운팅
    r_pluse = 0
    for i in range(f_len):
        if r_pluse == len(r):  # 오른쪽이 끝까지 갔을시엔
            arr.append(l[l_pluse])
            l_pluse += 1
        
        elif l_pluse == len(l):  # 왼쪽이 끝까지 갔을 시
            arr.append(r[r_pluse])
            r_pluse += 1
        
        elif l[l_pluse] <= r[r_pluse]:  # l이 크거나 같을때
            arr.append(l[l_pluse])
            l_pluse += 1
        
        else:  # 그 외에
            arr.append(r[r_pluse])
            r_pluse += 1
    return arr

T = int(input())  # 테케
for tc in range(1, T+1):
    arr_len = int(input())
    in_list = list(map(int, input().split()))
    ans = 0
    print(f'#{tc} {merge_sort(in_list)[arr_len//2]} {ans}')



