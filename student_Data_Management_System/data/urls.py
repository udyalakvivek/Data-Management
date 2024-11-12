from django.contrib import admin
from django.urls import path
from data import views

urlpatterns = [
    path('',views.show_Student_Data,name='Show_data'),
    path('add_Data/',views.add_Student_Data,name='Add_data'),
    path('update_Data/<int:id>/',views.edit_Student_Data,name='Update_data'),
    path('view_Single_Data/<int:id>/',views.single_Person_Data,name='Single_data'),
    path('delete_Data/<int:id>/',views.delete_Student_Data,name='Delete_data'),
    path('accounts/register/',views.register,name='Register'),
    path('accounts/login/',views.login,name='Login'),
    path('logout/',views.logout,name='Logout'),
]