from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Member_Data_Private, Member_Data_Public
from .forms import MembershipPublicDataForm
from checkout.models import MembershipPurchase
from checkout.forms import MembershipPrivateDataForm

# Create your views here.
@login_required
def dashboard(request, member_id):
    """ Display the member's dashboard """
    membership_purchase = MembershipPurchase.objects.filter(member=request.user)
    member_private = Member_Data_Private.objects.filter(member=request.user)
    member_public = Member_Data_Public.objects.filter(member=request.user)
    
    template = "user/dashboard.html"
    context = {
        'membership_purchase': membership_purchase,
        'member_private': member_private,
        'member_public': member_public,
    }

    return render(request, template, context)


@login_required
def edit_private_data(request, member_id):
    """ Update Member Private Account Data """
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


@login_required
def edit_public_data(request, member_id):
    """ Update Member Profile - Public Data """
    membership_purchase = MembershipPurchase.objects.filter(member=request.user)
    member_private = Member_Data_Private.objects.filter(member=request.user)
    member = get_object_or_404(Member_Data_Private, pk=member_id)
    member_public_exists = Member_Data_Public.objects.filter(member=request.user.id)
    
    public_data_form = MembershipPublicDataForm()

    # redirects the user back to the booking dashboard if they do not have
    # permissions to edit the booking
    if member.id != request.user.id:
        messages.error(
            request, "You do not have permissions to edit this booking.")
        return redirect('dashboard', member.id)
    
    if member_public_exists:
        member_public = get_object_or_404(Member_Data_Public, pk=member_id)
        public_data_form = MembershipPublicDataForm(instance=member_public)

        if request.method == "POST":
            public_data_form = MembershipPrivateDataForm(request.POST, instance=member_public)
            if public_data_form.is_valid():
                public_data_form.save()
                messages.success(request, "Your public profile changes saved successfully")
                return redirect('dashboard', member.id)
            else:
                messages.error(
                    request,
                    "Your changes could not be saved. Please check your form and try again",
                )

        public_data_form = MembershipPublicDataForm(instance=member_public)

    else:
        if request.method == "POST":
            public_data_form = MembershipPublicDataForm(request.POST)
            if public_data_form.is_valid():
                public_data = public_data_form.save(commit=False)
                public_data.member = request.user
                public_data.save()
                messages.success(request, "Your public profile changes saved successfully")
                return redirect('dashboard', member.id)
            else:
                messages.error(
                    request,
                    "Your changes could not be saved. Please check your form and try again",
                )

        public_data_form = MembershipPublicDataForm()
    
    template = "user/edit_public_data.html"
    context = {
        'member_public_exists': member_public_exists,
        'member_private': member_private,
        'member_public': member_public,
        'membership_purchase': membership_purchase,
        'public_data_form': public_data_form,
    }

    return render(request, template, context)


@login_required
def membership_purchases(request, member_id):
    """ View Member's Membership Purchase receipts """
    membership_purchase = MembershipPurchase.objects.filter(member=request.user)
    member_private = Member_Data_Private.objects.filter(member=request.user)

    template = "user/membership_purchases.html"
    context = {
        'membership_purchase': membership_purchase,
        'member_private': member_private,
    }

    return render(request, template, context)