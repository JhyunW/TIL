# SW Expert
# 파스칼의 삼각형

# 크기가 N인 파스칼의 삼각형을 만들려고함 즉 N줄의 삼각형
# 철 번째 줄은 항상 숫자 1 임
# 두번째 줄부터는 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성

T = int(input())  # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    arr = [[] * N for _ in range(N)]
    for i in range(N):
        for q in range(i+1):
            if q == 0 or i == q:
                arr[i].append(1)
            else:
                arr[i].append(arr[i-1][q-1] + arr[i-1][q])
    print(f'#{tc}')
    for w in arr:
        print(*w)