import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from order import models


def order(request):
    return render(request,'order.html')

@csrf_exempt
def createorder(request):
    order_request = (request.POST)
    print(order_request)
    models.Menuitem.objects.create(
        name=order_request['name'],
        description=order_request['description'],
        price=order_request['price'],
        category=models.category.objects.get(id=order_request['category'])
    )
    return JsonResponse({'massege':'recived order'})


def getorder(request):
    request_manu= models.Menuitem.objects.all()
    return  render(request,'order.html',{"fooditem":request_manu})
    return HttpResponseRedirect('http://127.0.0.1:8000/fresh/getorder/')


def about(request):
    return  render(request, 'About.html')
def service(request):
    return render(request,"service.html")
def payment(request):
    return render(request, "payment.html")

def contact(request):
    return render(request,'contact.html')




# @csrf_exempt
# def contactnext(request):
#
#     email = request.POST.get('email')
#     name = request.POST.get('name')
#     message = request.POST.get('message')
#     # models.contactme.objects.create(email==email, name==name, message==message)
#     p =contactnext(name=name, email=email, message=message),
#     p.save()
#     return HttpResponseRedirect("http://127.0.0.1:8000/fresh/contact/")
#     # if email== data.email and Password== data.Password:
#     #     return HttpResponseRedirect('http://127.0.0.1:8000/Home/')
#     #
#     #
#     # else:
    #     return HttpResponse("error")