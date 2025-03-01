from django.shortcuts import render
from .models import MembershipCategory


def all_categories(request):
    """ A view to show all the membership categories """

    categories = MembershipCategory.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'public/join.html', context)
