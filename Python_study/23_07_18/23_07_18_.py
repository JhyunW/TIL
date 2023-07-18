# 진법 변경
print(bin(12))
print(oct(12))
print(hex(12))
 # 실수 연산시 주의 사항
a = 3.2 - 3.1 # 0.1000000000000009
b = 1.2 - 1.2 # 0.0999999999999987

# 1. 임의의 작은 수 활용 1e-10 은 1의 -10 제곱
print(abs(a-b) <= 1e-10) # True 두수의 차이가 임의의 작은 수보다 작다면

# 2. math 모듈 활용
import math
print(math.isclose(a, b)) # True

# 지수(제곱하는 횟수) 표현 10^
print(314e-2)
print(314e2)


#Sequence Types 여러개의 값들을 순서대로 나열해서 저장하는 자료형
