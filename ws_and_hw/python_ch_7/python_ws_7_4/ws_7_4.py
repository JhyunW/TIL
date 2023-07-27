# ws_7_4.py

# 아래 클래스를 수정하시오.
class Shape:
   def __init__(self, x, y):
      self.x = x
      self.y = y


   def print_info(self):
      Width = self.x
      Height = self.y
      Area = self.x * self.y
      Perimeter = self.x * 2 + self.y * 2

      print(f'''Width:{Width}
Height: {Height}
Area: {Area}
Perimeter: {Perimeter}''')

shape1 = Shape(5, 3)
shape1.print_info()