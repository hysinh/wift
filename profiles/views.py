from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Member_Data_Private, Member_Data_Public
from checkout.models import MembershipPurchase
from checkout.forms import MembershipPrivateDataForm

# Create your views here.
@login_required
def dashboard(request, member_id):
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
def edit_private_data(request, member_id):
    """ Update Member Profile - Private Data """
    # member = request.user
    membership_purchase = MembershipPurchase.objects.filter(member=request.user)
    member_private = Member_Data_Private.objects.filter(member=request.user)
    member = get_object_or_404(Member_Data_Private, pk=member_id)
    
    # redirects the user back to the booking dashboard if they do not have
    # permissions to edit the booking
    if member.id != request.user.id:
        messages.error(
            request, "You do not have permissions to edit this booking.")
        return redirect('dashboard')

    if request.method == "POST":
        form = MembershipPrivateDataForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, "Member profile changes saved successfully")
            return redirect('dashboard', member.id)
        else:
            messages.error(
                request,
                "Your changes could not be saved. Please check your form and try again",
            )

    form = MembershipPrivateDataForm(instance=member)
    
    template = "user/edit_private_data.html"
    context = {
        'membership_purchase': membership_purchase,
        'member_private': member_private,
        'form': form,
        'member': member,
    }

    return render(request, template, context)