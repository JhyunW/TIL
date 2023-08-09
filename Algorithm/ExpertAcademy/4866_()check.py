T = int(input())

for tc in range(1, T+1):
    word = str(input())  # 단어 입력
    word_len = len(word)  # 단어의 길이 구하기
    arr = []  # 단어를 pop을 사용하기 위해 리스트에 넣어주기 위한 리스트
    for q in range(word_len):  # 단어를 한 글자씩 리스트에 추가
        arr.extend(word[q])

    box = []
    chek = []
    result = 1
    count = 0
    while count < word_len:
        if arr[count] == '(' or arr[count] == '{':
            box += arr.pop(count)
            word_len -= 1
        elif arr[count] == '}' or arr[count] == ')':
            if len(box) == 0:
                result = 0
                break
            elif arr[count] == '}' and box[-1] != '{' or arr[count] == ')' and box[-1] != '(':
                result = 0
                break
            else:
                box.pop(-1)
            count += 1
        else:
            count += 1
    if len(box) != 0:
        result = 0

    print(f'#{tc} {result}')
