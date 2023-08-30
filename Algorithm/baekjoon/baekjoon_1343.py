# baekjoon
# 1343_폴리오미노

bord = input()
check = ''
count = 0  # 4번째, 두번째 마다 A또는B블로으로 채워주기 위한 카운트
for i in range(len(bord)):  # 보드채워야 할 칸 반복
    if bord[i] == 'X':
        count += 1
        if count == 4:  # 만약 연속 4개가
            count = 0  # 카운트를 초기화 해주고
            for q in range(4):  # 4개의 A블록이 들어갈 시
                check += 'A'
    else:
        if bord[i] == '.':
            if count == 2:  # 카운트에 2가 쌓여있을 경우
                count = 0
                for q1 in range(2):  # 2칸인 B 블럭을 넣어줌
                    check += 'B'
                check += '.'
            elif count == 0:  # 카운트가 0 일경우
                check += '.'  # . 추가
            else:
                check = -1
                break
if count == 2:  # 카운트에 2가 쌓여있을 경우
    count = 0
    for q1 in range(2):  # 2칸인 B 블럭을 넣어줌
        check += 'B'
elif count != 0:  # 카운트 잔여가 남아있는데 끝날 경우
    check = -1

print(check)
