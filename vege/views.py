from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = "/login/")
def recipes(request):
    if request.method == "POST":

        data = request.POST  #for text data
        image = request.FILES.get('image')  #FILES for images and documents
        name = data.get("name")
        chef_name = data.get("chef_name")
        description = data.get("description")
        recipe_type = data.get("recipe_type")
        print(name,"\n",chef_name,"\n",description,"\n",image,"\n",recipe_type)

        #sending data to backend -  all data and login related things are written in Views
        Recipe.objects.create(
            name=name, 
            chef_name = chef_name,
            description=description,
            image=image,
            recipe_type=recipe_type)
    
        return redirect("/recipes/")
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search')) 
        #searches if the keyword enetered in search is found as substring in any recipe name

    context = {'recipes':queryset}
    return render(request, 'recipes.html', context)

@login_required(login_url = "/login/")
def update_recipe(request,id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')  #FILES for images and documents
        name = data.get("name")
        chef_name = data.get("chef_name")
        description = data.get("description")
        recipe_type = data.get("recipe_type")
    
        queryset.name = name
        queryset.chef_name = chef_name
        if image:
            queryset.image = image
        queryset.description = description
        queryset.recipe_type = recipe_type
        queryset.save()
        context = {'recipes':queryset}
        return redirect("/recipes/",context)
    
    conext = {'recipes':queryset}
    return render(request, "update_recipe.html",conext)

@login_required(login_url = "/login/")
def delete_recipe(request,id):
    print(id)
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    context = {'recipes':queryset}
    return redirect("/recipes/",context)

def login_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            user = authenticate(username = username, password = password)
            if user is None:
                messages.error(request,'Invalid Credentials')
                return redirect('/login/')
            else:
                #login page is used to sessions for any user.
                login(request, user)
                return redirect('/recipes/')
    
        else:
            messages.error(request,'Invalid Username and password combination')
            return redirect('/login/')
    
    return render(request, 'login.html')

def logout_page(request):
    #for logout
    logout(request)
    return redirect('/logout/')

def register_page(request):

    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        #setting password with encryption
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created succesfully')
        return redirect('/register/')
    
    return render(request, 'register.html')