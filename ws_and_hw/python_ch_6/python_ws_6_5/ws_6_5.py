# ws_6_5.py

# 아래 함수를 수정하시오.
def difference_sets(set_1, set_2):
    difference_result = set_1.difference(set_2)
    return difference_result

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)