"""start_django_2022_02_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
# from django.urls import include
from django.conf.urls import include
from django.conf.urls.static import static

from articleapp.views import ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view(), name='home'), # ip만 접속해서 쳤을경우 나와지는 곳
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + 부분이 media 사용할려면 필요함, media_url 과 media_root를 이어줌 => 서버가 정상적으로 이미지 보내줌