# SW Expert
# 5201_컨테이너 운반

def carrying():
    result = 0
    while T and W:  # 트럭 과 컨테이너 둘다 남아 있을경우 둘중 하나라도 바닥나면 종료
        if W[0] <= T[0]:  # 컨테이너가 실을 수 있는 무게 안에 들어갈 경우
            result += W.pop(0)
            T.pop(0)
        else:  # 트럭에 못실을 경우
            W.pop(0)

    print(f'#{tc} {result}')


T = int(input())  # 테케 입력
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    W = sorted(list(map(int, input().split())), reverse=True)  # 컨테이너의 무게
    T = sorted(list(map(int, input().split())), reverse=True)  # 트럭의 적재용량

    a = carrying()  # 함수 실행


