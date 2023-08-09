T = int(input())  # 테스트 횟수

for tc in range(1, T+1):    # 테스트 반복문
    word = str(input())  # 단어 입력
    word_len = len(word)  # 단어의 길이 구하기
    arr = []  # 단어를 pop을 사용하기 위해 리스트에 넣어주기 위한 리스트
    for q in range(word_len):  # 단어를 한 글자씩 리스트에 추가     줄이기 가능
        arr.extend(word[q])
    now = 0  # while문의 시작 점을 잡기 위한 now변수

    while now < word_len-1:  # arr의 index번호 밖으로 안나가기 위한 조건

        if arr[now] == arr[now+1]:  # 지금 인덱스의 값과 바로 앞의 값이 같을경우
            arr.pop(now+1)  # 앞에먼저 지우고 그다음 것도 지움
            arr.pop(now)
            word_len = len(arr)  # 길이를 다시 세어주고
            if now != 0:  # 시작점이 0이 아닌경우 다시 시작점을 잡아줌
                now -= 1
        else:
            now += 1  # 겹치지 않을경우 인덱스를 한칸앞으로 이동

    print(f'#{tc} {word_len}')
