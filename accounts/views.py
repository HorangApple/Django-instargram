from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    # 회원가입
    if request.method =="POST":
        # 직접 구현하면 취약성이 발생한다.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # form.user_set
            auth_login(request,user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})
    
def login(request):
    if request.method == "POST":
        # 실제 로그인(세션에 정보를 넣는다.)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # user 정보를 가지고 올 땐 get_user를 사용한다.
            auth_login(request,form.get_user())
        return redirect('posts:list')
    else:
        # 유저로부터 username과 비밀번호를 넣는다.
        form = AuthenticationForm()
        return render(request, 'accounts/login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('posts:list')