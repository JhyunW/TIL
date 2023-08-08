

def palindrome(s, word_length): # 문자열이 회문인지 비교하는 함수
    n = len(s)   # 문자열 길이
    mid = word_length // 2  # 비교를 위한 기준점
    count = 0 # 일치할 시 +1 을 할 카운트

    if n % 2 != 0:  # 홀수일 시
        left = mid - 1  # 시작점은 중앙에서 한칸 왼쪽
        right = mid + 1  # 끝점은 중앙에서 한칸 오른쪽
        while left >= 0 and right < n:  # 왼쪽은0, 오른쪽은 N 즉 범위를 벗어나지 않는동안 반복
            if s[left] == s[right]:  # 왼쪽 오른쪽 비교값이 같을시
                left -= 1  # 왼 오에 각각 -1 +1로 차이를 벌려주고 다시 while 진행
                right += 1
            else:  # 일치하지 않을시 while문 탈출
                break

            if right == n:  # 모든 문자열이 대칭이 될때에 카운트 1을 더하고 와일문 찰출
                count += 1
                break
    elif n % 2 == 0:  # 짝수일 시
        left = mid - 1  # 짝수는 기준의 -1 부터
        right = mid  # 기준점까지 를 시작점으로
        while left >= 0 and right < n:
            if s[left] == s[right]:
                left -= 1
                right += 1

            else:
                break
            if right == n:
                count += 1
                break

    return count


for tc in range(1, 11):  # 테스트 횟수
    arr = [[] for _ in range(8)] # 8줄의 리스트 생성

    word_len = int(input())

    for q in range(8):  # 각 줄마다 입력 넣기
        a = input()
        for w in a:
            arr[q].append(w)  # 리스트에 입력받은 한칸씩 넣어주기

    result = 0  # 대칭이되는 총 갯수

    for e in range(8):  # 세로 단어들 비교
        for e_1 in range(8-word_len+1):  # 리스트 범위를 벗어나지않게 범위를 8 - word_len + 1로 지정
            word_x =''  # 단어를 합칠 공간
            for r in range(word_len):  # 단어 길이반큼 반복해서 단어 합치기
                word_x += arr[e][e_1+r]

            result += palindrome(word_x, word_len)  # 나온 카운트값 더하기

    for e_3 in range(8 - word_len + 1):  # 리스트 범위를 벗어나지않게 범위를 8 - word_len + 1로 지정
        for e_4 in range(8):  # 가로 단어 비교
            word_y = ''  # 가로 단어를 합칠 공간
            for r in range(word_len):  # 단어 길이반큼 반복해서 단어 합치기
                word_y += arr[e_3 + r][e_4]

            result += palindrome(word_y, word_len)



    print(f'#{tc} {result}')





