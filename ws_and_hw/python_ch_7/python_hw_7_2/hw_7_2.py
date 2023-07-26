# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
   def repeat_string(self, number, text):
      #@staticmethod 함수를 추가해서 스태틱 사용도 가능
      for i in range(number):
         print(text)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")