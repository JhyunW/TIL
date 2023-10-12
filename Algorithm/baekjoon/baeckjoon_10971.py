# 백준 10971 외판원 순회
def move(now, money, deep):  # 현재의 줄, 현재 들은 비용, 깊이
    global short
    if money > short:  # 만약 현재돈이 최소값보다 커치면 가지치기
        return

    if deep == N-1:  # 마지막인 시작지점만 남겨놨을경우
        if arr[now][i] != 0:  # 시작지점으로 가는 길이 있다면,
            result = money + arr[now][i]
            if result < short:
                short = result
            return
    
    else:
        visited[now] = 1  # 시작지점은 1칠하기
        for q in range(N):
            if visited[q] == 0 and arr[now][q] != 0:
                visited[q] = 1
                move(q, money + arr[now][q], deep+1)
                visited[q] = 0


N = int(input())  # 도시의 수
arr = [list(map(int, input().split())) for _ in range(N)]  # N개의 arr
visited = [0] * N  # 방문 기록
short = 99999999  # 최소비용 기록 장소

for i in range(N):  # 모든 줄 즉 모든 경우의수를 구하기 위한 for문 시작지점이 안써져 있었기 때문
    move(i, 0, 0)  # i번째 줄, 0원, 0깊이

print(short)