from django.shortcuts import render,redirect  # 리다이랙트 추가
# 데코 임포트
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login  # 자동 로그인을 위한 함수
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm  # 로그인 창 폼
from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])  # 불러오고, 변경하는 작업 필요
def signup(request):  # 회원가입 함수
    # 로그인이 이미 되어있을 경우 -> 페이지를 메인으로 반환해주기
    if request.user.is_authenticated:  # 유저 정보가 있으면
        return redirect("boards:index")  # 메인페이지로 연결
    # 로그인이 안되어 있고, 변경사항이 올때 -> 생성
    if request.method == 'POST':
        # 가입 진행
        form = CustomUserCreationForm(request.POST)  # 폼스에 지정한 클래스에 POST를 넣어 반환
        if form.is_valid():
            user = form.save()  # 유저라는 함수에 내용을 저장하고
            auth_login(request, user)  # 자동 로그인을 위해 리퀘스트와 저장한 유저함수를 불러오기
            return redirect("boards:index")

    # 로그인이 안되어있고, 변경사항이 없을때
    else:
        # 회원가입 페이지를 계속 출력해주고 있어야함.
        form = CustomUserCreationForm()  # 회원가입 페이지 폼 불러오기
    
    # 불러온 폼을 콘텍스트 안에 딕셔너리 형태로 저장
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):  # 로그인 함수
    # 로그인한 사용자가 들어오면? -> 홈페이지로 보내기
    if request.user.is_authenticated:
        return redirect("boards:index")
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # 폼 안에 겟 유저로 유저정보 받기
            return redirect("boards:index")

    else:
        form = AuthenticationForm()   
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST  # 로그아웃 함수 만들기위해 필요한 데코
def logout(request):  # 로그아웃 함수
    # DB와 클라이언트 쿠키에서 세션 데이터 삭제
    # 로그인 안한 사용자가 요청을 보내면?
    if request.user.is_authenticated:
        auth_logout(request)  # 로그아웃을 하고
    return redirect("boards:index")  # 인덱스로 이동


def follow():  # 팔로우 함수
    # 회원 팔로우 데이터 저장 및 팔로우 데이터 삭제
    pass