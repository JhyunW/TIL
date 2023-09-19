# SW Expert
# 5208_전기버스2

def move(energy, now, use):  # 베터리, 현재위치, 사용베터리
    global count
    if use > count:
        return
    for moiving in range(energy):
        if now != goal:
            now += 1
            move(arr[now], now, use+1)  # 베터리, 현재위치, 사용베터리 불러오기
        
        if now == goal:  # 지금 위치가 골에 도달했을시
            if count > use:  # 지금 기록보다 더 적은 베터리 사용시
                count = use
                break






T = int(input())  # 테케
for tc in range(1, T+1):
    arr = list(map(int, input().split()))  # 버스 정류장 수, 베터리
    arr.append(0)

    goal = arr[0]  # 목표 인덱스
    B = arr[1]  # 베터리
    count = arr[0]  # 베터리 교체 횟수, 기본 최대치로 설정
    now_b = 0 # 현재 베터리 사용 횟수
    here = 1  # 현재 위치
    
    move(B, here, now_b)
    print(f'#{tc} {count}')
