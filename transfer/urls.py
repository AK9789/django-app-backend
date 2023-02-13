from django.urls import path, include
from .views import Transfer, HistoryList
urlpatterns = [
    path('transfer/<int:pk>', Transfer.as_view()),
    path('history/', HistoryList.as_view())
]