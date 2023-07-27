# hw_8_4.py
class BlankNameError(Exception):
    pass
# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        try:
            name = input('이름을 입력하세요')
            if not name:
                raise BlankNameError("이름을 입력 해 주세요.")
            age = int(input('나이를 입력하세요'))
            self.user_data['이름'] = name # 유저 인포 클래스에 있는 딕셔너리에 추가
            self.user_data['나이'] = age
            # or self.user_data = {'name':name, 'age':age}
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.') # 에러가 나올시 잡아내는곳
        return self.user_data
    def display_user_info(self):
        try:
            print('사용자 정보:')
            print('이름 : ',self.user_data['이름'])
            print('나이 : ',self.user_data['나이'])
        except KeyError:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()