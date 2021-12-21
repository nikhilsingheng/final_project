from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
         path('index/', views.index, name ='index'),
         path('signup/',views.signup,name='sign'),
         path('signup/Sign/', views.Sign, name='sign'),
         path('index/login/', views.login, name='login'),
         path('Home/', views.Home, name='login'),


         # path('login/',views.login,name='login')
]