# SW Expert
# 1223_계산기2
for tc in range(10):  # 테케
    len_arr = int(input())  # 식의 길이
    arr = list(map(str, input()))  # 식 입력
    stack = []  # *식을 먼저 처리하고 난 후의 식
    while arr:  # arr 리스트가 빌때까지
        a = arr.pop(0)

        if a == '*':  # 곱셈식이 먼저 되어야 하므로 곱셈식을 적용하여 스택에
            b = stack.pop(-1) * int(arr.pop(0))
            stack.append(b)

        elif a == '+':  # + 일 경우 그대로 스택에 넣기 (나중에 계산하기위함)
            stack.append(a)
        else:  # 그 외의 경우 숫자이므로 숫자 대입
            stack.append(int(a))

    result = stack.pop(0)

    while stack:  # 스택이 빌때까지
        a = stack.pop(0)
        if a == '+':  # 마지막 더하기 연산식 해주기
            result += stack.pop(0)

    print(f'#{tc+1} {result}')