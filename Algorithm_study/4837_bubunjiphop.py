# SW Expert
# 4837_부분 집합의 합

T = int(input())  # 테스트 케이스
for tc in range(1, T+1):
    arr = []
    for q in range(1, 12+1):
        arr.append(q)
    arr_len = len(arr)
    count = 0
    bit_total = []
    N, K = map(int, input())

    for i in range(1 << arr_len):  # 1 <<arr_len 부분 집합의 갯수
        sum_list = []
        for j in range(arr_len):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
                sum_list.append(arr[j])
            bit_total.append(sum_list)

    for q in range(len(bit_total)):
        if len(bit_total[q]) == N:

            sum_total = 0
            for w in range(len(bit_total[q])):
                sum_total += bit_total[q][w]
                if sum_total == K:
                    count += 1
