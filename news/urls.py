from . import views
from django.urls import path

urlpatterns = [
    path('', views.news_list.as_view(), name='news'),
    path('<slug:slug>/', views.news_detail.as_view(), name='news_detail'),
]