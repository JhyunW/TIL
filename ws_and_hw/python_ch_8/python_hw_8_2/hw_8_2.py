# hw_8_2.py

# 아래 함수를 수정하시오.
def check_number():
   try:
      number = int(input('숫자를 입력하세요'))
      if number > 0:
         print('양수입니다.')
         result = '양수입니다.'
      elif number < 0:
         print('음수입니다.')
         result = '음수입니다.'
      else:
         print('0입니다.')
         result = '0입니다.'
   except ValueError:
      print('잘못된 입력입니다.')
      result = '잘못된 입력입니다.'

      return result

check_number()

# 4번 실행
# for i in range(4):
#    check_number


# 입력이 잘못될 때까지 받기
# a = check_number()
# while a != '잘못된 입력입니다.':
#    a = check_number()


# 또 다른 방법으로는 while True: 를 받아서 하다가 test: except: 에 break 입력