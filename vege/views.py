from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse


def vege(request):
    if request.method == "POST":
        # Get data from the form
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')  # Get the uploaded image file
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        # Debugging: Print the received data
        print("Recipe Name:", recipe_name)
        print("Recipe Description:", recipe_description)
        print("Recipe Image:", recipe_image)  # To check if image is uploaded

        Receipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
        )
        return redirect('/recipes/')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
        
    return render(request, 'recipes.html', {'recipes': queryset})



def delete_recipe(request,id):
   queryset = Receipe.objects.get(id = id)
   queryset.delete()
   return redirect('/recipes/')


def update_recipe(request, id):  # Include 'id' in the function signature
    queryset = Receipe.objects.get(id=id)  # Retrieve the recipe by ID
  
    if request.method == "POST":
        data = request.POST
        # Update the recipe details based on form data
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image') 
       
        queryset.recipe_name =recipe_name
        queryset.recipe_description =recipe_description
        if recipe_image: 
          queryset.recipe_image =recipe_image

        queryset.save()
        
        return redirect('/recipes/')

    return render(request, 'update_recipes.html', {'recipe': queryset})
