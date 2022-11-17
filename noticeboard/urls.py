from django.urls import path
from . import views


app_name = 'noticeboard'

urlpatterns = [
    # path('', views.index, name='index'), # '' : 현재위치
    path('posts/', views.post_detail, name='posts'),
    path('response/', views.post_response, name='response'),
    #path('response2/', views.post_response2, name='response2'),
]