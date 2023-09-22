# SW Expert
# 2819_격자판의 숫자 이어 붙이기

# 이차원 배열
# 각 격자칸 0~9 숫자
# 현재 지점 +6번 이동하면서 숫자를 붙임
    # 이동은 4방향(델타)
    # 격자칸 다시 가도되면 -> visited 안써도 됨.

# 0시작 : 0102001
    # 숫자가 0으로 시작할 수 있네?
    # 문자열로 해결하면 편하겠다

# 요구하는 조건:
    # 서로 다른 일곱 자리 수들의 개수
    # 가지치기 불가능
    # 무조건 일곱 자리 수를 다 붙여봐야 함
    # 즉 완전탐색을 해야함

# 서로 다른 일곱 자리 수들의 개수
    #중복을 제거하는 방법 -> set자료 구조!

# 재귀 돌리면서 숫자를 붙인다
# 숫자가 7자리가 되면 set에 넣는다

# 특정 위치를 기점으로 상하좌우 문자를 붙여야 하므로
# 파라미터로 좌표값도 받아야 한다.

def dfs(y, x, number):
    if len(number) == 7:
        # 추가적인 작업
        return
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[x]

        # 갈 수 없는 위치면 continue
        if ny < 0 or ny >= 4:
            continue

        if nx < 0 or nx >= 4:
            continue

        # 갈 수 있다면, 다음 위치로 이동
        dfs (ny, nx, number + maps[ny][nx])


T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, T+1):
    # 서로 다른 수를 합친다 => 문자열이 더 좋다
    maps = [input().split() for _ in range(4)]

    # 7자리 수를 중복 제거하여 저장
    result = set()

    dfs()