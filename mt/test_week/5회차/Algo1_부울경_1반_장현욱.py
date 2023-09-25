def change(num):  # A~F로 바꿔주는 함수
    if num == 10 or num =='A':
        if num == 10:
            return 'A'
        else:
            return 10
    elif num == 11 or num == 'B':
        if num == 11:
            return 'B'
        else:
            return 11
    elif num == 12 or num == 'C':
        if num == 12:
            return 'C'
        else:
            return 12
    elif num == 13 or num == 'D':
        if num == 13:
            return 'D'
        else:
            return 13
    elif num == 14 or num == 'E':
        if num == 14:
            return 'E'
        else:
            return 14
    elif num == 15 or num == 'F':
        if num == 15:
            return 'F'
        else:
            return 15
    else:
        return int(num)
T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N
    P = str(input())  # 16진수 입력 -> 문자열이 들어올 수도 있으므로 str로 받음
    key = change(str(input()))  # key입력 -> 입력받은게 문자일경우 숫자로 변환
    result = []  # 숫자를 저장할 공간
    
    for i in P:  # P에 넣을 문자들을 반복문 돌리고
        if i == 'A':  # A ~ F 까지 각 문자열마다의 숫자를 if문으로 입력
            a = 10
            b = a ^ key
        elif i == 'B':
            a = 11
            b = a ^ key
        elif i == 'C':
            a = 12
            b = a ^ key
        elif i == 'D':
            a = 13
            b = a ^ key
        elif i == 'E':
            a = 14
            b = a ^ key
        elif i =='F':
            a = 15
            b = a ^ key
        else:  # 문자열이 아닐경우 숫자로 그대로 반환
            a = int(i)
            
        result.append(a^key)  # 나온 숫자에 ^ 를 대입해 저장
        
    print(f'#{tc}', end=' ')  # 테스트케이스 출력
    for q in result:
        if q > 9:  # 문자열로 넘어갈 경우 숫자로 변환하기위함
            b = change(q)
            print(b, end='')  # 나온 문자 출력
        else:
            print(q, end='')  # 나온 숫자 출력
    
    print()  # 다음줄

    