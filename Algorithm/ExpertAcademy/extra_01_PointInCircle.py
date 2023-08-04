# SW Expert
# 반지름이 N인 원안에 있는 격자점의 갯수 구학
# x^2 * y^2 <= N^2

t = int(input())

for tc in range(1, t+1):

    N = int(input()) # 반지름 길이
    count = 0 # 격자점 입력 받는 곳
    point_0 = (N * 4) + 1 # 4등분을 나눠서 계산할것이므로 중복되는 0이 오는 좌표값

    for x in range(1, N): # 0에서 한칸 띄우고 (1,1) ~ (N-1,N,1) 까지 반복
        for y in range(1, N):
            if (x * x) + (y * y) <= (N * N): # 예를들어 (0,1) 과 (0,-1) 즉 반으로 접었을때 반대쪽에 있는 점도 같이더함
                count += 4 # 면이 4개이므로 4개씩 카운트

    result = count + point_0 # 결과합산

    print(f'#{tc} {result}')
