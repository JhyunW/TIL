# url을 통해 같은 폴더에 있는 views.py에 있는 introduce 함수에게 str형식의 name, int형식의 age라는 변수를 전달하고 싶다. 
# 이때 __(a)__ , __(b)__에 들어 갈 코드를 작성하시오.

urlpatterns = [
    path('introduce/<name>/<int:age>',views.introduce)
    # 원래 받는게 str이기때문에 str:name을 안해줘도 되며, 하나마다 / 붙여주기
]
