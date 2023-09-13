"""
URL configuration for second_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # 각각의 폴더에서 관리하게 하기위한 명령어로, urls를 폴더별로 만들어주면 됨


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),  # articles/ 로 요청이 왔을때 articles라는 폴더 안에 urls 를 참고하세요 라는 뜻
    path('pages/', include('pages.urls'))
]
