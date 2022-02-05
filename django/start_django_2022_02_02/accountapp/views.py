from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_world(request):
    
    if request.method == "POST": #GET 인지 POST인지 구별해서 처리하게 해야한다.
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!'})
            #context 는 데이터 꾸러미라고 생각하면되고, text라는 이름을 가지고있고, 내용물은 POST METHOD
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})