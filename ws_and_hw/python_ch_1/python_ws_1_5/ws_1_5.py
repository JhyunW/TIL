#변수를 사용하지 않고 출력
print(3*2)
print(3**2)
print(3 ** 2 // (3 * 2), 3 ** 2 % (3 * 2))
print(3 ** 2 + ((-3) ** 2))
print() #공백

#변수를 사용하여 출력
three_x_two = 3*2
three_xx_two = 3**2
three_xx_division = 3 ** 2 // (3 * 2)
three_xx_remainder = 3 ** 2 % (3 * 2)
three_xx_negative = 3 ** 2 + ((-3) ** 2)

print("3의 2배의 값 : ", three_x_two)
print("3의 제곱 값 : ", three_xx_two)
print("3의 제곱 값에 3의 2배의 값으로 나눈 몫 : ", three_xx_division)
print("3의 제곱 값에 3의 2배의 값으로 나눈 나머지 : ", three_xx_remainder)
print("3의 제곱 값에 -3의 제곱 값을 더한 결과 : ", three_xx_negative)