# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(sort_tu):
  new_tuple = ()
  new_tuple = tuple(sorted(sort_tu))
  return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
