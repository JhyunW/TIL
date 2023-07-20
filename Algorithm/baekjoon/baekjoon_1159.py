# 농구 경기

number = int(input()) # 선수 숫자 등록

name = [input() for i in range(number)] # 선수 이름 리스트 등록

# print(name) 이름 입력이 잘 되었는지 확인

same_word = [] # 같은 첫글자 넣어두는곳
for i in name:
    same_word.append(i[0]) # 첫 글자만 불러오기

# print(same_word) 앞글자가 잘 뽑혔는지 확인

same_word_set = list(set(same_word)) # 첫 글자 중복 제거 넣어두기
same_word_set.sort() # 순서대로 정렬

#print(same_word_set) 글자 순서대로 정렬이 되었는지 확인

result = '' # 결과 값 / 조건에 충족하는 앞글자

for z in same_word_set: # 알파벳 for문으로 돌리기
    count = 0 # 몇명인지 카운트
    for x in name: # 이름 for문으로 돌리기
        if x[0] == z: # 앞글자가 중복된 문자랑 같을시 카운트
            count += 1
    
    if count >= 5: # 총 카운트가 5보다 높으면 추가
        result += z

if result == '': # 5개 이상의 중복이 없을 시
    print('PREDAJA')
else:
    print(result)

    

# for z in same_word_set:
