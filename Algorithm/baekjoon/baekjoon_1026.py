# 푸는중
# 길이가 N인 정수 배열 A,B가 있다. 다음과 같이 함수 S를 정의하자
# S = A[0] x B[0] + ... +A[N-1] x B[N-1]
# S의 최솟값을 출력하는 프로그램
def find_match_round(player1, player2):
    # 두 참가자의 번호를 입력받아 만날 차수를 계산하는 함수
    max_number = max(player1, player2)
    min_number = min(player1, player2)

    if max_number == min_number * 2:
        return 1

    # 두 수가 다른 2의 제곱수인 경우 다음 라운드로 넘어감
    return find_match_round((player1 + 1) // 2, (player2 + 1) // 2) + 1

# 7번과 8번이 만나는 차수 계산
player1 = 7
player2 = 8
result = find_match_round(player1, player2)
print(f"{player1}번과 {player2}번은 {result}차 대결에서 만납니다.")
