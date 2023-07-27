# ws_7_3.py

# 아래 클래스를 수정하시오.
class Shape:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   
   def calculate_perimeter(self):
      result = self.x * 2 + self.y * 2
      return result

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)