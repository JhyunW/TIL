T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    len_arr = len(arr)
    stack = []
    last = []
    result = 0
    number = []
    for q in range(len_arr):
        a = arr[q]  # 이번 비교 문자
        stack.append(arr[q])  # 스택에 쌓기

        if a == '(' or a == '{':  # (또는{가 와야하는데 비어있는경우
            last.append(a)
            if stack[0] != '(':
                result = -1
                break

        elif a == ')' or a == '}':  # )또는} 가 와야 하는데 비어있는경우
            if stack == []:
                result = -1
                break
            elif a == ')' and stack[-1] != '(':
                result = -1
                break
            elif a == '}' and stack[-1] != '{':
                result = -1
                break
            else:
                if last == '(':

                elif last == '{':
                last.pop

        else:
            number.append(a)
