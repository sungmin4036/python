from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    
    if request.method == "POST": #GET 인지 POST인지 구별해서 처리하게 해야한다.
        
        temp = request.POST.get('hello_world_input')
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        # DB에 저장하는 방법
        
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
                                                                                        #  temp -> new_hello_world 로 변경됨에 따라 객체로 처리 및 DB 처리
    
            #context 는 데이터 꾸러미라고 생각하면되고, text라는 이름을 가지고있고, 내용물은 POST METHOD
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})