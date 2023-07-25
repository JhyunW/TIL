# Q3. 리스트가 인자로 주어질 때, 리스트의 값을 모두 순회하여 
# 홀수인 경우 3배의 값을, 짝수인 경우 제곱의 값으로 변환하여
# 새로운 리스트 result에 담아 반환하는 
# 함수 make_odd_even를 작성하시오.

def make_odd_even(number_list):
    
    result = [i * 3 if i % 2 != 0 else i * i for i in number_list]
        #if 조건충족              #if 조건 부적합
    # result = []
    # for i in number_list:
    #     if i % 2 == 0:
    #         result.append(i*i)
    #     else:
    #         result.append(i*3)
    print(result)
    return result


# make_odd_even([1, 2, 3, 4, 5]) # [3, 4, 9, 16, 15]

make_odd_even([1, 2, 3, 4, 5])