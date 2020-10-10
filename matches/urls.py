from . import views
from django.urls import path


urlpatterns = [
    path('', views.match_list.as_view(), name='matches'),
    path('<slug:slug>/', views.match_detail.as_view(), name='match_detail')
]