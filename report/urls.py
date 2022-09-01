from django.urls import path
from .views import Index, Detail, Create

app_name = 'report'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<pk>/', Detail.as_view(), name='detail'),
    path('create/', Create.as_view(), name='create'),
]