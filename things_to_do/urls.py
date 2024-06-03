from django.urls import path, include
from . import views

app_name =  'things_to_do'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:activity>/', views.activity_detail, name='activity_detail'),
]