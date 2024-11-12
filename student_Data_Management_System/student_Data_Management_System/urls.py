from django.contrib import admin
from django.urls import path, include
from data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('data.urls')),
    path('register/',views.register,name='Register')
]
