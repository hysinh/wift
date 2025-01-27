from django.shortcuts import render


def view_basket(request):
    return render(request,'user/basket.html')
