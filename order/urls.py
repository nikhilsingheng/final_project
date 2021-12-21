from django.urls import path

from . import views
from django.conf.urls.static import static

urlpatterns = [
          path('ram/', views.order, name ='index'),
          # path('nikhil/',views.createorder, name= "creatorder")
          path('nikhil/',views.createorder, name='nikhil'),
          path("getorder/",views.getorder, name='getorder'),
          path("about/",views.about, name='about'),
          path("service/",views.service, name='service'),
          path("payment/", views.payment, name='payment'),
          path('contact/',views.contact, name='contact'),
          # path('nimit/',views.contactnext, name= 'contactnext')
          # path('Home/',views.Home, name='home')


]