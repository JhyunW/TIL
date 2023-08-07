# 바운스 첼린지
# 팅기는 거리는 0, 1, 2, 3 식으로 N까지 증가

T = int(input())  # 테스트 케이스
for tc in range(1, T+1):
    N = int(input())  # 탁자에 있는 N개의 정수
    arr = []  # 배열 생성
    arr = list(map(int, input().split()))  # 각 칸의 숫자 입력

    result = 0  # 모든 게임의 총합
    for q in range(N):  # arr 리스트를 반복
        this_game = 0  # 매 라운드의 총점수
        for w in range(0, N, q+1):  # 0부터 시작 하여 매 라운드마다 뛰는 폭이 1씩 증가하는 반복문
            if w > N: # 만약 배열의 길이를 벗어나면 for문 벗어나기
                break

            else:  # 그렇지 않을경우 각각의 인덱스 점수를 더하기
                this_game = this_game + arr[w]
        result += this_game  # 이번 턴에서 나온 점수를 총합
        if result < 0:  # 만약 점수가 0점 아래일경우 0점으로 표기
            result = 0
    print(f'#{tc} {result}')  # 결과