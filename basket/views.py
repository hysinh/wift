from django.shortcuts import render
from membership.models import MembershipCategory
from membership.forms import RegistrationForm


def view_basket(request):
    """ A view to display the basket """
    form = RegistrationForm()
    context = []

    # If user inputs a membership level by click on the corresponding
    # button on the Join page, this will set the membership selection
    # as the initial value in the membership registration form
    if request.method == "GET":
        selected_membership = request.GET.get('category')
        form = RegistrationForm(initial={'name': selected_membership})

    categories = MembershipCategory.objects.all()
    context = {
        'form': form,
        'categories': categories,
    }
    
    return render(request,'basket/basket.html', context)
