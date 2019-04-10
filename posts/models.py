from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    
    def __str__(self):
        return "{}".format(self.content)