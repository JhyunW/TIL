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

    for e in range(8 - word_len + 1):  # 세로열 비교
        for e_1 in range(8):
            e_arr = []
            for e_2 in range(word_len):
                e_arr.append(arr[e + e_2][e_1])

            if e_arr == e_arr[::-1]:
                result += 1

    print(f'#{tc} {result}')

