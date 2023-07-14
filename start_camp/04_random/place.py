import random

# 1. 우리반 학생 전체 명단 리스트 만들기
students = ['강성은','강주원','고유한','김연빈','김지수','황성주','김해인','문지호','박주헌','이수빈','배준형','손종민','신현기','옥세훈','이승집','이준우','이흔오','장현욱','정지헌','정창휘','조혜원','최용훈','최재성','탁윤희',]
    #print(student)
# 2. 리스트를 무작위로 섞어주는 라이브러리 사용하기
random.shuffle(students)
    #print(student)
# 3. 리스트를 순회해서 학생 이름 출력
#for student in students:
#    print(student)
# for index in range(0, len(students), 6):
#     for i in range(6):
#         print(students[index + i], end = ' ')
#     print()
# 4. 자리 모양에 맞춰서 출력
# 5. 출력 모양 꾸미기
print('======================스크린======================')
print('                                           김구현')
print()
for index in range(0, len(students), 6):
     for i in range(6):
         if i != 0 and i % 3 == 0:
              print('      ', end = ' ')
         print(students[index + i], end = ' ')
     print()
# 6. ctrl + alt + 방향키 위, 아래 ㅣ 포커싱 크기 증가
# 7. cyrl + 방향키 ㅣ 단어 기준으로 이동 가능
# 8. alt + 방향키 ㅣ 포커싱 되어있는 줄 위치 이동
