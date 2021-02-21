from django.urls import path
from . import views


app_name = 'Notice'


urlpatterns = [
    path('list/', views.CommentNoticeList, name='list'),
    path('update/', views.CommentNoticeUpdate, name='update'),
]
