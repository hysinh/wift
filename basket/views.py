from django.shortcuts import render
from membership.models import MembershipCategory
from membership.forms import RegistrationForm


def view_basket(request):
    """ A view to display the basket """
    form = RegistrationForm()
    categories = MembershipCategory.objects.all()
    context = {
        'form': form,
        'categories': categories,
    }
    
    return render(request,'basket/basket.html', context)
