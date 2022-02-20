from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project
# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)# 지울때 article이 회원 탈퇴시 개시글이 사라지지않고, 알수없음으로 표시되는것/ user객체에서 artice 접근시 사용하는 이름 article
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True) # auto_created 자동생성시 시간 자동으로 넣어줌