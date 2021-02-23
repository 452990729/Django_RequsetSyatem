from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post-comment/<int:project>/', views.post_comment, name='post_comment'),
    path('post-comment/<int:project>/<int:parent_comment_id>/', views.post_comment, name='comment_reply')
]
