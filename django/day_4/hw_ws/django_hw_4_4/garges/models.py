from django.db import models

# Create your models here.
# 파이썬 클래스 정의 -> 아이디어 스케치
class Garage(models.Model):
    # id 컬럼은 직접 정의 안한다.
    # 장소
    location = models.CharField(max_length=200)
    # 용량
    capacity = models.IntegerField()
    # 주차 가능 여부
    is_parking_avaliable = models.BooleanField()
    # 여는시간
    opening_time = models.TimeField()
    # Field 뒤에 호출() 생략하는 경우 있는데
        # variable = class 할당
    # class_variable = models.class() 인스턴스 생성
    # 닫는시간
    closing_time = models.TimeField()

# 저장과 setting 에 추가 잊지말기
# python manage.py makemigrations -> 설계도 작성
# python manage.py migrate 로 저장

# 조회
# ORM -> python Object 다루는법
# myModel ClassName.manager.Queryset API
garages = Garage.objects.all()
print(garages)

# 생성
# Python Object
# 객체 하나 생성 ( 인스턴스 생성 )
# garage = Garage()
# garage.location = '부산시 강서구'
# garage.capacity = 10
# garage.is_parking_avaliable = True
# garage.opening_time = '07:00'
# garage.closing_time = '23:00'

# # save메서드 호출
# garage.save()

# QuerySet API
# 생성 완료된 경우, 완료된 객체 반환
# Garage.objects.create(location='경상남도 창원시',
#                     capacity=20,
#                     is_parking_avaliable = False,
#                     opening_time = '07:00',
#                     closing_time = '23:00',
#                     )

# garages = <queryset []>

# 1번 독도가 없다면 새 데이터 생성 후 조회출력
garage = Garage.objects.filter(location = '울릉도')
if len(garage) == 0:
    Garage.objects.create(location = '독도', 
        capacity = 40,
        is_parking_avaliable = True,
        opening_time = '09:00',
        closing_time = '23:00')
    garage = Garage.objects.filter(location = '독도')

print(garage)

garage_capacity = Garage.objects.filter(capacity__lte = 30)
print(garage_capacity)
# gte = greater than equal  >=  미쳤다 진짜
# lte = less than  <= 

for garage_true in garages:
    if garage_true.is_parking_avaliable == True:
        print(garage_true.location)