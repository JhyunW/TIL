# SW Expert
# 5203_베이비진 게임

def jhin():
    for i in range(len(card)):
        if i % 2 != 0:  # 홀수번의 순서에 1번 플레이어 카드
            player_1.append(card[i])
        else:  # 짝수번의 순서에 2번 플레이어 카드
            player_2.append(card[i])




T = int(input())  # 테케

for tc in range(1, T+1):
    card = list(map(int, input().split()))
    player_1 = []
    player_2 = []

