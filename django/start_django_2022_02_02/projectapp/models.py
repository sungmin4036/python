from distutils.command.upload import upload
from pydoc import describe
from turtle import title
from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): # 프로젝트 이름 정상적으로 나오게 하기 위해서
        return f'{self.pk} : {self.title}' # f'' 를 사용하면 직접 변수를 출력할수 있게 해준다.