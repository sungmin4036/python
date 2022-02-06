from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from accountapp.models import HelloWorld
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def hello_world(request):
    
    if request.method == "POST": #GET 인지 POST인지 구별해서 처리하게 해야한다.
        
        temp = request.POST.get('hello_world_input')
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        # DB에 저장하는 방법
        
        hello_world_list = HelloWorld.objects.all()
        # DB 저장된것 가져오는것, all 은 HelloWorld의 모든 객체 가져온다.
        
        return HttpResponseRedirect(reverse('accountapp:hello_world')) # accountapp 에있는 hello_world로 재접속해라.
        # return HttpResponseRedirect('account/hello_world')
        # 기존에는 리턴시 브라우저가 똑같이해도 똑같이저장
        # POST가 렌더가 하는게 아닌, get으로 되돌아가서, 이 일을 반복하지 않아도 되는것을 만들기 위해 HttpResponseRedirect사용
        
    
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) # hello_world_list 라는 이름에 hello_world_list 객체를 담아서
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
                                                                                        #  temp -> new_hello_world 로 변경됨에 따라 객체로 처리 및 DB 처리
    
            #context 는 데이터 꾸러미라고 생각하면되고, text라는 이름을 가지고있고, 내용물은 POST METHOD
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    
    
    
# CBA 형식의 클래스 만드는곳.
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 성공했다면, hellow_word 로 재연결 해라, reverse 는 함수형 에서사용하고, reverse_lazy는 클래스형
    template_name = 'accountapp/create.html' # 회원가입 할떄, 비주얼 어떤걸 이용할것인지.
    