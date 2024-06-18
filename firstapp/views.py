from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# def welcome(request):
    # return HttpResponse("Welcome to Django😁")

def home(request):
    context ={
        "title": "Home page",
        'description': "Welcome to the homepage!"
    }

    return render(request, "home.html", context) 

def about(request):
        context = {
            "title" : "About me",
            "description" : "Learn more about me"
        }
    
        return render(request, 'about.html', context) 
    
def contact(request):
       context = {
           "title" : "Contact me",
           "description" : "Let's chat😁"
       } 
       
       return render (request, "contact.html", context)

def index(request):
       post = Post.objects.all()
       return render(request, 'index.html',{'posts':post})
   