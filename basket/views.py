from django.shortcuts import render, redirect, reverse, get_object_or_404
from membership.models import MembershipCategory
from profiles.forms import RegistrationForm


def view_basket(request):
    """ A view to display the basket """
    form = RegistrationForm()
    context = {}

    # If user inputs a membership level by click on the corresponding
    # button on the Join page, this will set the membership selection
    # as the initial value in the membership registration form
    if request.method == 'GET':
        selected_membership = request.GET.get('category')
        form = RegistrationForm(initial={'membership_level': selected_membership})

    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         registration = form.save(commit=False)
    #         registration.save()

    #         return redirect('checkout')
    #     else:
    #         context = {'form': form}

    #         messages.error(
    #         request, "Please choose a membership level to proceed")

    #         return render(request, 'basket/basket.html', context)

    categories = MembershipCategory.objects.all()
    context = {
        'form': form,
        'categories': categories,
    }
    
    return render(request,'basket/basket.html', context)


def view_basket_test(request):
    """ A view to display the basket """
    form = RegistrationForm()
    context = {}

    # If user inputs a membership level by click on the corresponding
    # button on the Join page, this will set the membership selection
    # as the initial value in the membership registration form
    if request.method == 'GET':
        selected_membership = request.GET.get('category')
        form = RegistrationForm(initial={'membership_level': selected_membership})

    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         registration = form.save(commit=False)
    #         registration.save()

    #         return redirect('checkout')
    #     else:
    #         context = {'form': form}

    #         messages.error(
    #         request, "Please choose a membership level to proceed")

    #         return render(request, 'basket/basket.html', context)

    categories = MembershipCategory.objects.all()
    context = {
        'form': form,
        'categories': categories,
    }
    
    return render(request,'basket/basket.html', context)


def add_to_basket(request, category_id):
    """ Add an annual memebership to the basket """

    selected_membership_level = get_object_or_404(MembershipCategory, pk=category_id)
    quantity = 1        
    basket = request.session.get('basket', {})

    if category_id in list(basket.keys()):
        basket[category_id] += quantity
    else:
        basket[category_id] = quantity
        
    request.session['basket'] = basket

    return reverse('view_basket_test')


def add_to_basket_test(request, category_id):
    """ Add an annual memebership to the basket """

    selected_membership_level = get_object_or_404(MembershipCategory, pk=category_id)
    quantity = 1        
    basket = request.session.get('basket', {})

    basket.clear()
    basket[category_id] = quantity
        
    request.session['basket'] = basket
    print(request.session['basket'])

    return redirect('view_basket_test')



