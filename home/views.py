from django.shortcuts import render

# Create your views here.

# WIFT Public pages
def index(request):
    """ A view to return the index page """
    return render(request, 'public/index.html')

def about(request):
    """ A view to return the about page """
    return render(request, 'public/about.html')

def fellowships(request):
    """ A view to return the Programs page """
    return render(request, 'public/fellowships.html')