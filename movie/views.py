from django.http import HttpResponse
from django.shortcuts import render
from .forms import contactform

def index (request):
    context={
        "title":"Hello homepage",
        "content":"Welcome to the homepage"
    }
    return render(request, "homepage.html", context)


    # def details(request, movie_id):
    #     return HttpResponse("<h2>welcome Movie id : " + str(movie_id) + "</h2>")


def about(request):
    context = {
        "title": "about page",
        "content":"Welcome to about us page"
    }
    return render(request, "homepage.html",context)

def contact(request):
    contact_form = contactform()
    context = {
        "title": "contact page",
        "content":"Welcome to contact page",
        "form" : contact_form
    }
    if request.method == "POST":
        #print(request.POST)
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('password'))
    return render(request, "contact/index.html", context)