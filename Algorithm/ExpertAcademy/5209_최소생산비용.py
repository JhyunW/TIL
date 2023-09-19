# SW Expert
# 5209_최소 생산 비용

def production(line, pluse):  # 몇번라인, 가격 합
    global result
    if pluse > result:  # 만약 나온 값이 지금 최저보다 높을 시
        return
    
    if line == N:  # 모든 라인을 돌고 난 후
        result = pluse  # 가격이 초과할 경우는 위에서 이미 걸러냄.
        return
    
    else:
        for i in range(N):  # N번 만큼 반복
            if visited[i] == 0:
                visited[i] = 1  # 1을 칠하고 탐색 시작
                production(line+1, pluse + arr[line][i])  # 현재 라인의 몇번 제품 가격
                visited[i] = 0  # 이 라인이 1번일 경우의 탐색을 다 끝낸후 지우기



T = int(input())  # 테케
for tc in range(1, T+1):
    N = int(input())  # 공장, 제품 갯수
    arr = []
    for _ in range(N):  # 공장별 단가 입력
        arr.append(list(map(int, input().split())))
    result = sum(sum(arr, []))  # 최소 값 저장할 공간 , 처음엔 모든 숫자의 합으로
    visited = [0] * N  # 생상 기록

    production(0, 0)
    print(f'#{tc} {result}')
    