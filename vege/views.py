from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
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
    return render(request, 'recipes.html')

