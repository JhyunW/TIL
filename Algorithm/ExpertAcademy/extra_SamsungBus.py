t = int(input()) # 테스트 케이스 입력

for tc in range(1, t + 1):
    bus_station = [0] * 5001  # 5000개의 버스 노선 매 시도마다 초기화
    go = int(input())  # 버스 노선
    for go_ing in range(go): # 노선 반복
        ai, bi = map(int, input().split()) # 노선 시작점과 끝점 입력

        for bus_plus in range(ai, bi + 1): # 버스가 지나가는 정류장마다 +1
            bus_station[bus_plus] += 1

    result = [] # 결과값을 저장할 공간

    P = int(input())  # 보고싶은 정류장 갯수
    for check in range(P): # 보고싶은 정류장 넘버
        where = int(input())
        result.append(bus_station[where]) # 결과 넣어주고

    print(f'#{tc}', *result) # 리스트 풀어서 출력
