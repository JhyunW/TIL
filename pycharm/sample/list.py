import sys
sys.stdin = open('input.txt')
# 테스트 케이스
t = int(input())
for tc in range(t):
    # 방의 가로 길이 즉 상자가 담겨있는 칸의 개수
    N = int(input())
    # 쌓인 상자의 개수
    # 공백을 기준으로 나눠서 받음
    boxes = list(map(int, input().split()))
    max_v = boxes[0]
    min_v = boxes[0]
    # 첫번째 칸에서 마지막 칸까지 몇번이 이동 가능할지, 나보다 크거나 같은 갯수
    result = 0
    for i in range(N):
        # i 번째 상자가 덜어질 수 있는 최대
        # 방해받지 않고 떨어지는 최대
        # 전체 길이 - (내 위치 + 1인덱스가 0번부터 시작하기 때문)
        max_H = N - (i+1)
        # 내 다음 오는 상자들 중에
        # 나보다 크거나 같은 값들 찾기
        # 내 다음부터 끝까지
        for j in range(i+1, N):
            # 내 높이보다, j번째 위치가 크거나 같은 값
            if boxes[i] <= boxes[j]:
                max_H -= 1
            # i 번째 값이 최대로 떨어질 수 있는 낙차 값이
            # 현재 내가 기록해둔 최종 결과값보다 크다면,
            if result < max_H:
                result = max_H
    print(f'#{tc + 1} {result}')