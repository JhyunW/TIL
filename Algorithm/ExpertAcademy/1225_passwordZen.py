# 8개의 숫자를 입력 받는다
# 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다
# 다음 첫 번째 수는 2감소한 뒤, 맨 뒤로 보낸다
# 이런식으로 그다음은 3 그다음은 4 감소해서 뒤로보낸다
# 숫자가 감소할때 0보다 작아지면 0으로 유지되며 프로그램 종료
# 그리고 나온 숫자가 암호로 선정

for _ in range(10):
    tc = int(input())  # 테스트 케이스 번호
    arr = list(map(int, input().split()))

    count = 0  # 1~5 순회 하는 카운트
    while arr[-1] != 0:  # 마지막 번호가 0이 올때까지
        count += 1  # 매 반복마다 카운트 증가
        arr.append(arr.pop(0) - count)
        if count == 5:  # 만약 카운트가 5가 될시 초기화
            count = 0
        if arr[-1] < 0:  # 만약 마지막 숫자가 0보다 작아지면 0으로 초기화
            arr[-1] = 0

    print(f'#{tc}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()

# 1~5 순회 하는거 % 나머지로 돌릴수 있음
