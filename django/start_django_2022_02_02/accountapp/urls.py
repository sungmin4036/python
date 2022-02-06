from django.urls import path
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, hello_world, AccountUpdateView
from django.contrib.auth.views import LoginView, LogoutView



app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    
    
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # 클래스형은 중간에 이것을 추가해 줘야 한다.
    
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    # 특정 유저의 정보를 볼려면, 계정의 ID 필요 즉 Primary Key, pk라는 이름의 int 형의 정보를 받겠다.
]