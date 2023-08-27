import sys
sys.stdin = open('input.txt')

# SW Expert
# 1860_진기의 최고급 붕어빵

# 0초부터 붕어빵을 만들며, M초의 시간을 들여 K개의 붕어빵을 만들 수 있음
# 0초 이후에 손님들이 언제도착하는지 주어지면 모든 손님들에게 기다리는 시간 없이
# 붕어빵 제공이 가능한지 판별하는 코드 작성
# 즉 손님이 기다리는 시간이 없이 K개의 붕어빵이 제공이 가능한지 판별

T = int(input())  # 테케

for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N명의 고객, M초 마다 K개의 붕어빵
    N_time = sorted(list(map(int, input().split())))  # 고객들의 도착 시간

    box = 0  # 붕어빵 보관함
    result = 'Possible' # 결과
    go = N_time[-1]

    if N_time[-1] == 0 and M != 0:  # 오픈런 반례
        result = 'Impossible'
    for i in range(go+1):  # 손님이 오는 시간의 가장 마지막 시간까지 반복
        if result == 'Impossible':  # box가 음수로 가면 for문 종료 또는 고객이 다 빠졌을시
          break
        if i != 0 and i % M == 0:
            box += K  # 일정 시간마다 K개의 붕어빵 더하기
        while N_time and N_time[0] == i:
            if box == 0:
                result = 'Impossible'
                break  # 박스에 붕어빵이 없을 경우 while문 종료
            else:
              box -= 1
              N_time.pop(0)
    print(f'#{tc} {result}')
