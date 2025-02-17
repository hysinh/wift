from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Member_Data_Private, Member_Data_Public
from checkout.models import MembershipPurchase
from checkout.forms import MembershipPrivateDataForm

# Create your views here.
@login_required
def dashboard(request):
    """ Display the member's dashboard """
    membership_purchase = MembershipPurchase.objects.filter(member=request.user)
    member_private = Member_Data_Private.objects.filter(member=request.user)
    
    template = "user/dashboard.html"
    context = {
        'membership_purchase': membership_purchase,
        'member_private': member_private,
    }

    return render(request, template, context)


@login_required
def edit_private_data(request):
    """ Display the user's dashboard """
    member = request.user
    membership_purchase = MembershipPurchase.objects.filter(member=request.user)
    member_private = Member_Data_Private.objects.filter(member=request.user)
    member = get_object_or_404(Member_Data_Private, pk=member.id)
    
    # redirects the user back to the booking dashboard if they do not have
    # permissions to edit the booking
    if member.id != request.user.id:
        messages.error(
            request, "You do not have permissions to edit this booking.")
        return redirect('dashboard')

    form = MembershipPrivateDataForm(instance=member)
    
    template = "user/edit_private_data.html"
    context = {
        'membership_purchase': membership_purchase,
        'member_private': member_private,
        'form': form,
        'member': member,
    }

    return render(request, template, context)