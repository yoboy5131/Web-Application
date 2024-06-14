from django.urls import path
from . import views

urlpatterns = [
   
    path('add-admission/', views.add_admission, name='add_admission'),
    path( 'signup/',views.signup,name= 'signup'),
    path('login/',views.login,name='login'),
    path('admissions/',views.admissions_list, name='admissions')
]
