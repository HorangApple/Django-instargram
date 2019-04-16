from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

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
    
def profile(request,username):
    # username을 가진 유저의 상세 정보를 보여주는 페이지
    profile = get_object_or_404(get_user_model(),username=username)
    return render(request, 'accounts/profile.html', {'profile': profile})
    
def delete(request):
    # method == POST : 계정을 삭제한다. == DB에서 user를 삭제한다.
    if request.method == "POST":
        request.user.delete()
        return redirect('posts:list')
    # method == GET : 진짜 삭제하시겠습니까?
    else :
        return render(request, 'accounts/delete.html')