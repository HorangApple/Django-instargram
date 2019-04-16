from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    # TextField로 선언하면 form이 textarea로 반영된다.
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    # User와의 연결고리 (외래키) (1:N)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User와의 연결고리 (외래키) (N:M) Like, posts_post_like_users 테이블 생성
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    
    def __str__(self):
        return "{}".format(self.content)
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}".format(self.content)