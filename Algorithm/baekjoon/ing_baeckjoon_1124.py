# 1124_언더프라임

# 예를들어 12를 소인수 분해하면 2, 2, 3 이 나오는데 이렇게 나온
# 숫자들의 갯수가 소수이면 그 수를 언더프라임 이라고 한다.
# A 보다 크거나 같고 B보다 작거나 같은 정수 범위 안에서 언더프라임인 것의 갯수를
# 구하시오

# 시간초과 해결해보기
A, B = map(int, input().split())  # 최소 A, 최대 B

all_result = 0  # 최종결과

for length in range(A, B+1):  # A 부터 B 까지 정수 하나하나 불러오기
    count = 0 # 해당 숫자의 소수 갯수  즉 길이가 소수인지 확인 해야함
    result = 0  # 두번째 소인수
    div = 2  # 나눌 숫자 1은 안하므로 2 부터 시작해서 하나씩 늘려갈 예정
    while length != 1:  # 숫자가 나눠서 0이 될때까지
        if length % div == 0:  # 나눴을때 나머지가 없이 나눠지면
            length = length / div  # 그 값으로 나누기
            count += 1
        else:
            div += 1
        
        if div > 17 and count == 1:
            count = 2  # 17 이상까지 맞는게 없으면 프라임
            break
    
    div = 2  # 다시 나눌 수 초기화

    while count != 1: 
        if count % div == 0:  # 갯수가 소수일때
            result += 1  # 길이의 소수 갯수
            count = count / div  # 나눌 수 지정, 나오는게 두개일경우만

        else:
            div += 1

        if result > 1:
            break
    
    if result == 1:
        all_result += 1

print(all_result)
