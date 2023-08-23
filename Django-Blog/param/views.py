from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import Blog,Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     return render(request,"index.html")
def home(request):
    blog1=Blog.objects.all()
    cat1=Category.objects.all()
    p=Paginator(blog1,1)
    p_no=request.GET.get('page')
    p_all=p.get_page(p_no)
    return render(request,"home.html",context={"blog1":blog1,"cat1":cat1,"p_all":p_all})

@login_required
def about(request):
    form=BlogForm(request.POST,request.FILES)
    if request.method=="POST": 
        if form.is_valid():
            form.save()
        return redirect('home')
    form=BlogForm()
    return render(request,"about.html",context={"form":form})

def show(request,id):
    show1=[Blog.objects.get(id=id)]
    return render(request,"show.html",context={"show1":show1})

def Edit(request,id):
    instance=Blog.objects.get(id=id)
    form=BlogForm(request.POST,instance=instance)
    if request.method=="POST": 
        if form.is_valid():
            form.save()
        return redirect('home')
    form=BlogForm(instance=instance)
    return render(request,"edit.html",context={"form":form})

def delete(request,id):
    del1=Blog.objects.get(id=id)
    del1.delete()
    return redirect('home')

def login_user(request):
    if request.method=="POST":
        r=request.POST
        user1=r.get('username')
        pass1=r.get('password')
        user=authenticate(username=user1,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('about')
    return render(request,"login.html")

def logout_user(request):
    logout(request)
    return redirect('home')