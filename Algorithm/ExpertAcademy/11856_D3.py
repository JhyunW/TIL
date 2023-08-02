# SW Expect
# 11856_반반_D3

test_case = int(input()) # 테스트 횟수 입력

for test in range(test_case): # 테스트 횟수만큼 반복

    word = input() # 단어입력받기

    same_num = set(word) # set을 사용하여 중복 문자 합치기
    # 이번 문제같은경우 4 문자열이라는 조건과 2개씩 짝일경우
    # 라는 조건이 있어 Yes 가 나올려면 무조건 set의 길이는
    # 2가 나와야함
    if len(same_num) == 2:
        print(f'#{test+1} Yes')

    else:
        print(f'#{test+1} No')

