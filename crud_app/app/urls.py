from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.user_login,name='user-login'),
    path('contact/',views.contact,name='contact'),
    path('data/',views.data,name='data'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('add-student/',views.insertData,name='insertData'),
    path('update/<id>',views.updateData,name='updateData'),
    path('delete/<id>',views.deleteData,name='deleteData'),
    path('success',views.succes,name="sucess"),


    
]
