
from django.shortcuts import render,redirect
from django.contrib.auth import logout


from item.models import Category,Item
from .forms import SignupForm
from django.contrib import messages
# Create your views here.
def index(request):#information about browser :reuqest
  items=Item.objects.filter(is_sold=False)[0:6]
  categories=Category.objects.all()
  return render(request,'core/index.html',{
    'categories':categories,
    'items':items,
  })
def  contact(request):
  return render(request,'core/contact.html')
def signup(request):
  if request.method=='POST':
    form=SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/login/')
  else:
    form=SignupForm()
  return render(request,'core/signup.html',{
    'form':form
  })
def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect('core:index')