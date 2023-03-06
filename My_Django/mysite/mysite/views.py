from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def Hello(request):
    return HttpResponse("Hello World")  # HttpResponse返回的是一个字符串



