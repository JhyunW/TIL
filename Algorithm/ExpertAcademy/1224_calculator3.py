# SW Expert
# 1224_계산기3
for tc in range(10):  # 테케
    len_arr = int(input())  # 식의 길이
    arr = list(map(str, input()))  # 식 입력
    stack_1 = []  # 전체를 담을 식
    stack_2 = []  # 괄호를 처리할 식
    stack_3 = 0  # 스택2를 풀때 더하기를 할 식
    while arr:  # arr 리스트가 빌때까지 / 괄호를 풀어주는 식
        a = arr.pop(0)
        b = 0
        if a == ')':  # 닫는 괄호를 만났을 시
            stack_2.append(stack_1.pop(-1))

            while b != '(':  # 다시 여는 괄호를 만나기전까지 반복
                b = stack_1.pop(-1)  # stack_1에서 맨 뒤의 문자를 가져오고
                if b == '*':  # 곱셈식을 먼저
                    stack_2.append(int(stack_2.pop(-1)) * int(stack_1.pop(-1)))
                elif b == '+':  # 더하기 식일경우 일단 순서 보류를 위해 스택2에 저장
                    stack_2.append(b)
                elif b == '(':  # 닫는 괄호가 나올시 스택2에 쌓인 식을 계산해주기 위해
                    while stack_2:  # 스택2가 빌때까지 반복
                        c = stack_2.pop(0)  # c변수에 따로 하나씩 불러오며 확인
                        if c != '+':  # +의 경우 스택3번에 숫자를 계속 더해주고
                            stack_3 += int(c)
                    stack_1.append(stack_3)   # 나온 결과를 다시 스택1에 넣어줌
                    stack_3 = 0  # 그리고 스택3 초기화
                    #  +,* 를 한 후 stack_1에 저장
                else:
                    stack_2.append(b)  # 숫자의 경우엔 스택2에 저장해주기
        else:  # 숫자와 +기호의 경우 스택에 저장해주기
            stack_1.append(a)
    print(f'#{tc+1} {stack_1[0]}')
