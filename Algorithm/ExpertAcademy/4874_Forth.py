# SW Expert
# 4874_Forth

T = int(input())

for tc in range(1, T+1):
    sick = list(map(str, input().split()))  # 식을 입력받을 공간
    list_len = len(sick)  # 반복문을 돌리기위한 입력받은 값의 길이
    result = []  # 결과를 저장하기 위한 공간
    try:  # 예외가 나올시 error을 출력하기 위해 사용
        for i in range(list_len):  # sick의 길이만큼 반복
            if sick[0] == '+':  # + 가 올시
                a = result.pop(-2)  # pop을 사용하여 변수를 삭제, 대입
                b = result.pop(-1)
                result.append(a+b)
                sick.pop(0)
            elif sick[0] == '-':  # - 가 올시
                a = result.pop(-2)
                b = result.pop(-1)
                result.append(a - b)
                sick.pop(0)
            elif sick[0] == '*':  # * 가 올시
                a = result.pop(-2)
                b = result.pop(-1)
                result.append(a * b)
                sick.pop(0)
            elif sick[0] == '/':  # / 가 올시 나누어떨어지므로 //로 처리
                a = result.pop(-2)
                b = result.pop(-1)
                result.append(a // b)
                sick.pop(0)
            elif sick[0] == '.':  # . 이 나올시 마지막 예외인 result에 하나가 아닐경우 처리 / 그 외의 경우 값 저장
                if len(result) != 1:
                    result = 'error'
                else:
                    result = result[0]
            else:
                result.append(int(sick.pop(0)))  # 숫자가 나올경우 result 변수에 저장
    except:
        result = 'error'

    print(f'#{tc} {result}')

