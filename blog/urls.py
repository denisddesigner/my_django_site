from django.urls import path
from . import views

urlpatterns = [

    # 127.0.0.1:8000 ---> localhost
    # mydjangosite.com --> online
    path('', views.post_list, name='post_list'),

    # 127.0.0.1:8000/post/2 ---> localhost
    # mydjangosite.com/post/2 --> online
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.1:800/post/new ---> localhost
    # mydjangosite.com/post/new --> online
    path('post/new/', views.post_new, name='post_new'),
]