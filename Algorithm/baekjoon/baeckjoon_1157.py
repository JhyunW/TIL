# 단어공부

# 알파벳 대소문자가 주어지고 그 안에서 가장 많이 사용된
# 알파벳이 무엇인지 알아보는 프로그램
# 단 대소문자는 구분하지 않음


word = input() # 단어 입력받기
word_lo = word.upper() # 대소문자 구분을 없애기 위해 대문자로 통일
count_1 = 0 # 포문마다 일시적으로 저장할 값
count_2 = 0 # 처음 포문의 최대값
result_al = '' # 가장 많이 사용된 알파벳

for i in range(ord('A'), ord ('Z')+1):
    i_result = chr(i)
    count_1 = word_lo.count(i_result)
    if count_2 < count_1:
        count_2 = count_1
        result_al = i_result

for z in range(ord('A'), ord ('Z')+1):
    i_result = chr(z)
    count_1 = word_lo.count(i_result)
    if result_al == i_result:
        continue
    elif count_2 == count_1:
        result_al ='?'

print(result_al)