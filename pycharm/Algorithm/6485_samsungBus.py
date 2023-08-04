# SW Expert
# 1~5000 개의 버스정류장엔 5000까지의 번호가 붙어있음
# 버스노선은 N개가 있으며, i 번째 버스 노선은 번호가 Ai 이상이며
# bi 이하인 모든 정류장만을 다니는 버스 노선이다
# p개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지
# 구하는 프로그램을 작성하라라

t = int(input()) # 테스트 케이스

for tc in range(1, t+1):
    N = int(input())
    cnt = [0] * 5001 # 1번부터 5000까지
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1         # 현재 노선선

    p = int(input())
    bus_stop = [int(input()) for _ in range(p)]
    print(f'#{tc}', end = ' ')
    for x in bus_stop:
        print(cnt[x], end = ' ')
    print()