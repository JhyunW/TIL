# 입력 받는 값
# N = 운동을 할 시간 m = 최소맥박 M = 최대맥박
# T = 운동시 추가맥박 R = 휴식시 떨어지는 맥박

# 조건 N 분을 운동하기 위해 필요한 최솟값
# 맥박은 최대 M을 넘으면 안되고 m보다 낮아질 수 없다

N, m, M, T, R = map(int,input().split())

center = m # 기준 맥박

count_t = 0 # 운동 시간
count_r = 0 # 쉰 시간
if m + T > M : # 기준점에서 운동을 한번도 못하는 상황
        print(-1)
else:
    while N != count_t: # 목표 시간이랑 같아질동안 반복
            if m < center:
                  m = center
            if m + T <= M:
                m += T
                count_t += 1
            else:
                  m -= R
                  if m < M : 
                        m == M # 기준점보다 높아질경우 최대 수치로 반환
                        count_r += 1
                  else:
                        count_r += 1

    print(count_r + count_t)