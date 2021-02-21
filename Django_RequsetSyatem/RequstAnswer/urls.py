from django.urls import path,re_path
from . import views

urlpatterns = [
    path('new/', views.CreateNew, name="CreateNew"),
    path('index/', views.Index, name="Index"),
    path('sub/', views.SubIndex, name="SubIndex"),
    path('sub/<str:project>/', views.SubDetail, name='SubDetail'),
    path('sub/<str:project>/check/', views.CheckProject, name='CheckProject'),
    path('<str:project>/', views.Detail, name='Detail'),
    path('<str:project>/del/', views.Del, name='Del'),
    path('', views.Index, name="Index"),
]
