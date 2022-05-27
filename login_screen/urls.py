from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register_new_user/', views.register_new_user, name='user_register'),
    path('login/', views.loginview,name='user_login'),
]