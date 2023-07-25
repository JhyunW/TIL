# ws_6_4.py

# 아래 함수를 수정하시오.
def get_keys_from_dict(dict_keys):
    result = dict_keys.keys()
    return result

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)