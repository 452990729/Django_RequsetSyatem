"""Django_RequsetSyatem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import notifications.urls
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings
from Login import views
from RequstAnswer import views as RequstAnswerViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.WebHome),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('mod/', views.ModUser, name="ModUser"),
    path('home/', views.HomePage, name="HomePage"),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notice/', include('Notice.urls', namespace='notice')),
    path('captcha', include('captcha.urls')),
    path('RequstAnswer/', include(('RequstAnswer.urls', 'RequstAnswer'), namespace='RequstAnswer')),
    path('Comment/', include(('Comment.urls', 'Comment'), namespace='Comment')),
    re_path(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path('Upload/', RequstAnswerViews.Upload),
    path('', views.WebHome),

]
