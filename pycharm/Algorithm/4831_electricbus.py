# 전기버스 문제 다시 풀어보기
t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int, input().split())

    while True:
        # 충전소