# SW Expert
# 1486_장훈이의 높은 선반 안되넹..비교해보기

# 서점
# 높이가 B인 선반
# 키가 큰 장훈이는 자유롭게 이용
# 원하는 물건을 쌓기위해 탑을 쌓음
# 탑을 쌓는 방법
    # 1명 : 점원의 키 == 탑 높이
    # 2명 이상: 점원키의 합 == 탑의 높이
# 높이가 B 이상인 탑 중에서, 높이가 가장 낮은 탑을 구해라

def recur(level, acc_height):
    global ans
    # 가지 치키
    # 현재까지 탑이 선반 높이를 넘어간다면
    # 앞으로는 더 볼 필요가 없다
    if acc_height >= B:
        ans = min(ans, acc_height)
        return
    
    # 기저 조건
    if level == N:
        return
    
    # 들어 가기 전 트리형식으로 생각 중복제거
    # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + arr[level])
    # 안 쓸 경우
    recur(level + 1, acc_height)

    # 다음 재귀 함수 호출

    # 돌아왔을 때


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = list(map(int, input().split()))
    ans = int(1e9)
    recur(0, 0)
    print(f'#{tc} {ans - B}')