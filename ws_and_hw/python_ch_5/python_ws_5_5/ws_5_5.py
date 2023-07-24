# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(number):
    two_list = []
    for i in range(len(number)):
        a = number.pop(0)
        if a % 2 == 0:
            two_list.extend([a])
    return two_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)