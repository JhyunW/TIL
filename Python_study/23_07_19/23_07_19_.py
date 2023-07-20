# 함수 활용
def make_sum(pram1, pram2):
    '''
    이것은 두 수를 받아
    두 수의 합을 반환하는 함수
    
    >> make_sum(1,2)
    3
    '''
    return pram1 + pram2

# 팩토리얼 사용
def factorial(n):
    # 종료 조건 : n이 0이면 1을 반환하고 종료
    if n == 0:
        return 1 # 1을 호출
    
    # 재귀 호출 : n과 n - 1 의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1) # 식을 호출

# 팩토리얼 계산 예시
result = factorial(5)
print(result)


# 맵 함수 이용 예시
numbers = [1, 2, 3]
result = map(str, numbers)

print(result) # 0x000001E6EA303FA0>
print(list(result)) # ['1', '2', '3']

result_1 = []
for number in numbers:
    result_1.append(str(number))

print(result_1)

# zip 사용 예시
girls = ['jane', 'ash']
boys = ['peter', 'park']
paris = zip(girls, boys)

print(paris)
print(list(paris)) # dict로도 사용 가능

# map과 lambda 같이 사용

numbers_1 = [1, 2, 3, 4, 5]
result_2 = list(map (lambda x: x * 2, numbers_1))
print(result_2)


# scope 예시
age = 100  # 글로벌

def parent_func(): # 부모라는 로컬의 age 주소에 30
    age = 30

    def child_func(): #  아이라는 로컬의 age 주소에 20
        age = 20
        print(age, 'child_func') 

    child_func() 
    print(age, 'parent_func')

parent_func() # 글로벌 age라는 주소에 = 100
print(age, 'global')

# scope 예시2
global_var = '글로벌 값'
def updatate_value(global_var):  # 매게 변수 -> local scope
    print(global_var, '매개 변수로 받은 값') 
    result_4 = global_var * 3  # 글로벌 변수가 가지고 있던 값 활용 가능
    global_var = '로컬 값' # 글로벌 변수에 할당된 값에 영향 없이 다른값 재할당 가능

    return result_4

