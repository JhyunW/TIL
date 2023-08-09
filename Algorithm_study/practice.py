for tc in range(1, 11):  # 테스트 횟수
    arr = [[] for _ in range(8)]  # 8줄의 리스트 생성

    word_len = int(input())  # 비교 문장 길이

    for q in range(8):
        arr[q].append(input())  # 리스트에 입력

    result = 0  # 대칭되는 문자열 수

    for w in range(8):  # 가로열 비교 반복문
        for w_1 in range(8 - word_len + 1):
            if arr[w][w_1 : w_1 + word_len] == arr[w][w_1 : w_1 + word_len][::-1]:  # 문자열을 뒤집어도 똑같을시
                result += 1

    for ee in range(8 - word_len + 1):  # 세로열 비교 한줄씩 내려가는 반복문
        for e in range(8):  # 왼쪽부터 오른쪽까지 도는 반복문
            e_arr = []  # 세로 단어를 합칠 리스트
            for e_1 in range(word_len):  # 세로로4개의 문자 가져오기 위한 포문
                str_in = arr[e_1 + ee][0]  # 한 줄씩 가져오기
                e_arr.append(str_in[e])  # 가져온 줄의 e번째 글자 가져와서 리스트에 추가

            e_result = [''.join(e_arr)]  # 가져온 단어들을 합치기
            e_reverse = e_result[0][::-1]  # 뒤집어보기
            if e_result == e_reverse:
                result += 1

    print(f'#{tc} {result}')

