from django.shortcuts import render
from .forms import PostModelForm

# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기.
        pass
    # GET 요청이 오면
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request,'post/create.html', context)