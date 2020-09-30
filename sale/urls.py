
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.UserCreate.as_view(), name='account-create'),

]
