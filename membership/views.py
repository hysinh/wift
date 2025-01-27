from django.shortcuts import render
from .models import Category

def all_categories(request):
    """ A view to show all the membership categories """

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'public/join.html', context)
