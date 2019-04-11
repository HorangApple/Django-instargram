from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post

# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기.
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
        
    # GET 요청이 오면
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request,'post/create.html', context)

def list(request):
    # 모든 Post를 보여줌
    posts=Post.objects.all()
    return render(request,'post/list.html',{
        'posts':posts,
    })
    
def delete(request,post_id):
    post=Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:list')
    
def update(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        # 수정내용 DB에 반영
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        # 수정내용 편집
        form = PostModelForm(instance=post)
        context = {
            'form': form,
        }
        return render(request,'post/update.html',context)