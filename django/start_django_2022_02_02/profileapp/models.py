from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    # Profile과 User를 연결해준다. , on_delete는  연결되어있는 USER 계정이 delete 시 그와 연결된 Profile 객체를 어떻게 할것인지, 
    # CASCADE는 같이 삭제한다라는 의미, related_name 은 따로 profile 객체를 차지 않더라도 바로 찾을수있게 이름을 정의한것

    image = models.ImageField(upload_to='profile/', null=True)
    # 이미지 파일을 서버에 저장되는데, 어디에 저장될지 경로 실제 media/profile/ 에 저장된다. null=ture 는 사진이 없어도 등록 가능하다.

    nickname = models.CharField(max_length=20, unique=True, null=True)
    # unique 무조건 유일한 닉네임 가져야한다.

    message = models.CharFiled(max_length=100, null=True)
    