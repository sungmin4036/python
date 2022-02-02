from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hellow_world(request):
    return HTTPResponse('안녕하세요')