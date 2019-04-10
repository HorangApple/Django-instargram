from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label="content")
    
    class Meta:
        model = Post
        # '__all__'은 모델이 갖고있는 모든 것을 가져옴
        # input을 만들 칼럼 값을 list로 만들어 넣어줌.
        fields = ['content',]