# ws_7_2.py

# 아래 클래스를 수정하시오.
class Shape: 
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def calculate_area(self):
      result = self.x * self.y
      return result
      
shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)