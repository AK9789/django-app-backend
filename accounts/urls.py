from django.urls import path, include
from .views import  login, GetUser, Register

urlpatterns = [
    # path('hello-view/', HelloApiViews.as_view()),
    path('login/', login.as_view()),
    path('user/', GetUser.as_view()),
    path('register/', Register.as_view())
]