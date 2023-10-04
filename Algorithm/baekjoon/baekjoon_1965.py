# 백준
# 1965_상자넣기

def find(num, now, size):  # 순서, 현재기록, 박스크기
    global best
    if best == N:  # 최대 횟수일 경우
        return
    if num == N:  # N번까지 돌았을 경우 현재의 최고 숫자와 비교
        if now > best:
            best = now

    else:
        for i in range(num, N):  # 현재 횟수부터 N까지
            if arr[i] > size:  # i번째 박스가 지금의 박스 크기보다 크면
                find(i+1, now+1, arr[i])  # 해당 경우의 수 함수를 호출

N = int(input())  # 상자의 갯수
arr = list(map(int, input().split()))  # arr 입력

best = 0  # 최대 횟수

find(0, 0, 0)
print(best)