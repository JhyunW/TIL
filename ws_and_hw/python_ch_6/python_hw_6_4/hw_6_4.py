# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(main_dict, key, value):
    new_dict = main_dict.copy()
    new_dict.setdefault(key, value)
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)