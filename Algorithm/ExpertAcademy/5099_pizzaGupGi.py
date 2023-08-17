# SW Expert
# 5099_피자굽기

# N개의 피자를 동시에 구울수 있는 화덕이 있음
# 1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣음
# 치즈의 양에따라 녹는 시간이 다름
# 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램
# 치즈가 한번 들어갈때마다 C // 2 로 줄고
# 모두녹아 0이 되면 화덕에서 꺼내고 남은 피자를 넣음

T = int(input())  # 테케
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 화덕칸, 피자갯수
    pizza = list(map(int, input().split()))  # 치즈의 양

    pizza_num = []  # 피자 번호 할당할 공간
    for q in range(M):  # 피자 번호 넣어주기
        pizza_num.append(q+1)

    pizza_num_in = []  # 화덕에 들어간 피자의 번호

    arr = []  # 화덕 리스트

    for i in range(N):
        arr.append(pizza.pop(0))  # 화덕의 칸에 피자를 순서대로 채우고 넣은 피자 제거
        pizza_num_in.append(pizza_num.pop(0))  # 각가의 번호에 맞게 넣어주고 제거
# Ex) (7, 2, 6)  피자치즈
#     (1, 2, 3)  피자번호
    while len(arr) != 1:  # 남은 화덕속의 피자가 1개일때까지 반복
        a = arr.pop(0) // 2  # a 변수에 화덕에 구워지는 치즈의 //2 를 반환
        b = pizza_num_in.pop(0)  # 동시에 그 피자의 번호도 b변수에 반환

        if a == 0 and len(pizza) != 0:  # 치즈가 다 녹고, 남은 피자가 있을시
            arr.append(pizza.pop(0))
            pizza_num_in.append(pizza_num.pop(0))

        elif a != 0:  # 피즈가 녹지 않았을 경우 다시 뒤로 보내기
            arr.append(a)
            pizza_num_in.append(b)

    print(f'#{tc} {pizza_num_in[0]}')