# articles
from django.urls import path
from . import views  # 현재 폴더에 있는 views 로부터 불러오도록 하겠다는 뜻
app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    # variable routing
    path('<int:number/>', views.random_number, name='random_number')
]