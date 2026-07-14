from django.urls import include, path
from . import views
urlpatterns = [
  
    path('',views.welcome),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.Home,name='home'),
    path('delete/<int:input_id>',views.Delete,name='delete'),
    path('edit/<int:input_id>',views.Edit,name='edit'),
    path('create/',views.create,name='create'),
    path('logged_out/',views.Logout,name='logged_out')
]