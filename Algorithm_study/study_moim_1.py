N = int(input())  # N개의 고유한 번호를 가진 부품
N_num = list(map(int, input().split()))  # 부품별 번호 입력
M = int(input())  # M개 종류의 부품
M_num = list(map(int, input().split()))  # 필요한 부품 번호 입력
N_sort = sorted(N_num)  # 부품 번호를 크기 순으로 정렬
for q in M_num:  # 찾는 부품들 순회
    start = 0  # 시작점
    end = N  # 끝 점
    result = 0  # 있으면 인덱스 번호 넣는곳...
    while start <= end:  # 시작점이 끝점보다 작거나 같을동안
        mid = (start + end) // 2  # 중간값 구하기

        if N_sort[mid] == q:  # 만약 중간값이 같으면
            result = mid  # 리절트값에 추가
            break
        elif N_sort[mid] < q:  # 중간 값보다 크면
            start = mid + 1  # 시작 지점을 중간지점+1부터 이유는 중간지점은 이미 체크했으므로 중간보다 앞에서
        else:
            end = mid - 1  # 중간 값보다 작다면 끝 지점을 mid-1로 교체

    if result == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')
