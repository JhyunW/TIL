# ws_6_1.py

# 아래 함수를 수정하시오.
def union_sets(set_1, set_2):
    set_all = set_1.union(set_2)
    return set_all

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)