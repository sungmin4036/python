from django.db import models

# Create your models here.
                    # Model의 상속을 받는것으로, 빵틀에서 원초적인 모델을 가져와서 추가적인 정보를 입력하고, 그것을 새로운 클래스(모델)로 만드는것
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) # 모델 안에있는 캐릭터 필드를 가지고 오는것. null 은 db에서 null에대한 허용 하는지에대한 설정, 널 허용X => 무조건 있어야한다.
    