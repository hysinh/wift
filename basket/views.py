from django.shortcuts import render
from membership.models import Category
from membership.forms import RegistrationForm


def view_basket(request):
    """ A view to display the basket """
    form = RegistrationForm()
    context = {}

    
    return render(request,'user/basket.html')
