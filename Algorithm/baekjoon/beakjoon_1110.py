#더하기 사이클

# ex) 26 -> 2+6 -> 6+8 -> 8+4 -> 4+2 -> 26 돌아옴

n = str(input()) #처음 값 받음

if int(n) <= 9: # 입력받은 수가 1의 자리일 경우 십의자리에 0 추가
    ten = 0
    n_1 = str(ten) + n # 입력받은 수를 문자열로 변환하여 n_1에 저장
    n_next = n[0] + n_1[-1] # 처음 입력받은 10의 자리와 문자열로 변환한 앞의자리 문자열로써 합침
else: # 나머지 경우의 수 계산
    ten = int(n[0]) # 십의 자리를 숫자로 변환
    one = int(n[-1]) # 일의 자리를 숫자로 변환

    n_1 = str(ten + one) # 구한 두 수를 더한 후 문자열로 변환해서 저장

    n_next = n[-1] + n_1[-1] # 처음 입력한 수의 십의 자리와 문자열로 변환한 수의 일의 자리를 붙임

n_result = int(n_next) # 붙인 결과값을 인트로 변환하여 result 에 저장

count = 1

n_number = int(n) # 와일문 비교를 위해  처음 입력한 수를 인트로 변경
while n_number != n_result:
    
    ten = int(n_next[0])
    one = int(n_next[1])

    n_1 = str(ten + one)

    n_result = int(n_next[-1] + n_1[-1])
    n_next = n_next[-1] + n_1[-1]


    count += 1

print(count)