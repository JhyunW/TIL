# 1124_언더프라임

# 예를들어 12를 소인수 분해하면 2, 2, 3 이 나오는데 이렇게 나온
# 숫자들의 갯수가 소수이면 그 수를 언더프라임 이라고 한다.
# A 보다 크거나 같고 B보다 작거나 같은 정수 범위 안에서 언더프라임인 것의 갯수를
# 구하시오

# 시간초과 해결해보기  count가 16개 이상이면 끝
A, B = map(int, input().split())  # 최소 A, 최대 B

prime = [0] * 100001
print(prime)
all_result = 0  # 최종결과

for i in range(2, 100000):  # 2부터 10000까지 확인
    print(i)
    count = 0 # 해당 숫자의 소수 갯수  즉 길이가 소수인지 확인 해야함
    now = i  # 현재 숫자
    div = 2  # 나눌 숫자 1은 안하므로 2 부터 시작해서 하나씩 늘려갈 예정
    while now != 1:  # 숫자가 나눠서 0이 될때까지
        if now % div == 0:  # 나눴을때 나머지가 없이 나눠지면
            now = now // div  # 그 값으로 나누기
            count += 1
        else:
            div += 1
        
        if div > 17 and count == 0:
            print(i)
            prime[i] = 1  # 17 이상까지 맞는게 없으면 프라임 이므로 체크
            break

        if now == 1:
            div = 2
            result = 0
            while count != 1:
                if count % div == 0:
                    result += 1
                    count = count // div
                else:
                    div += 1
                if result > 1:
                    break
                else:
                    prime[i] = 1

print(prime)

