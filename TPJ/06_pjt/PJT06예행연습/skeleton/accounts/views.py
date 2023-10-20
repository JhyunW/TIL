from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods ,require_POST  # 로그아웃에 사용
from django.contrib.auth import login as auth_login  # 자동로그인 기능을 위함
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm  # 로그인 할때 활용
from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인한 사용자가 들어오면 boards.index로 보내겠다
    if request.user.is_authenticated:
        return redirect("boards:index")
    
    # METHOOD가 GET일때와 POST일때 분기
    # POST : 실제로 회원가입을 진행해야함
    if request.method == 'POST':
        # 사용자의 입력을 폼에 담아라
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # 만약 제대로 들어왔다면
            user = form.save()  # 저장해라 ( 셀프.인스턴스 반환 저장하려는 객체를 반환)
            auth_login(request, user)  # 자동 로그인 기능
            return redirect("boards:index")

    # GET : 회원가입 페이지 보여줘야함
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인한 사용자가 들어오면??
    if request.user.is_authenticated:
        return redirect("boards:index")
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():  # 만약 제대로 들어왔다면
            auth_login(request, form.get_user())  # 자동 로그인 기능
            return redirect("boards:index")

    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def logout(request):  # 세션 데이터를 삭제 즉 DB를 건듦 즉 POST를 불러오기
    # 로그인 안된 사용자가 요청을 보내면?
    if request.user.is_authenticated:  # 만약 로그인 되어 있다면
        auth_logout(request)
    return redirect("boards:index")  # 그 후 인덱스로 보냄, 버튼은 직접 구현해보기