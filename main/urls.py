from django.urls import path

from main import views


urlpatterns = [
    path('hello/', views.hello),
    path('hello2/', views.hello2)
]