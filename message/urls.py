from django.urls import path, include
from .views import Messagefunc, Requestfunc

urlpatterns = [
    path('message/', Messagefunc.as_view()),
    path('request/', Requestfunc.as_view())
]