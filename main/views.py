from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def hello2(request):
    return render(request, 'hello.html')
