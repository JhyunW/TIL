from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout as auth_logout
# Create your views here.
def signup(request):
    # 사용자가 요청을 보낸 method에 따라 조건 분기해서 서로 다른 일처리
    if request.method == 'POST':  # 데이터 CREATE 해달라는 뜻
        # 사용자가 작성해서 보낸 데이터로 User Create
        '''
            user = accounts.User()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password')
            user.save()
        '''
        # 유저 생성을 위헤 필요한 각 필드들에 대한 정보 -> User 모델에 있음
        # User 모델에 대한 정보 -> ModelForm에 있음
        # form 인스턴스 만들때 request.POST에 있는 데이터를 포함해서 만들면?
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # 유효성 검사
            user = form.save()  # 저장 -> DB에 반영
            # redirect 의 첫번째 인자로 작성해야 하는 내용?
                # 사용자를 어디로 보낼 것인지 (어떤 경로로 요청한 것으로 취급할 것인지.)
                # redirect('app_name:pattern_name')
                # redirect('pattern_name')
                # redirect('url')
            # redirect 함수가 하는 일은 무엇인가?
                # 작성된 to 위치로 GET요청을 보냄
            auth_login(request, user)
            return redirect('main')
    else:  # 그 외인 경우에는 회원가입 페이지 보여 달라는 뜻
    # 회원가입 버틀 클릭 -> 회원가입 할 수 있는 페이지 보여줘
    # 회원가입 할 수 있는 페이지를 사용자에게 반환
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    # 렌더 함수가 하는 일 : html 파일 렌더링
    # BASE_DIR/app/templates/accounts/signup.html
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        # 사용자가 보내준 데이터로 form을 생성
        form = AuthenticationForm(request, request.POST)
        # 인증 이라는 행위는.. -> db에 있는 username과 password와
        # 사용자가 보내준 username과 password가 일치하기만 하면된다
        # db를 생성하거나 하는 행위는 없다.
        if form.is_valid():
            # 유효성 검사 문제 없으면 '로그인' 행위를 한다
            # 로그인이란, 현재 사용자가 보내준 데이터를 기반으로 특정유저를 찾는다.
            # 그 특정 유저에 대한 정보를 암호화해서 사용자에게 돌려준다.
            # 사용자는 다음 요청부터는 넘겨받았던 데이터를 함께 동봉해서 보낸다.
            # 서버는 그렇게 사용자가 보내준 암호화된 데이터를 토대로 유저를 인식한다.

            # 요청보낸 유저가 누군지 알아야지 auth_login함수도 실행이 되겠지?
            auth_login(request, form.get_user())
            return redirect('main')  # 로그인 후 해당 페이지로 보냄.

    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    # 세션에서 연결된 user 정보 제거
    if request.method == 'POST':
        # request에는 현재 로그인 되어 있는 유저 정보가 포함되어있다.
        auth_logout(request)
    return redirect('accounts:login')  # 어디로 보낼지