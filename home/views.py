from django.shortcuts import render, redirect
from membership.models import MembershipCategory
from membership.forms import RegistrationForm
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

# WIFT Public pages
def index(request):
    """ A view to return the index page """
    return render(request, 'public/index.html')

def about(request):
    """ A view to return the about page """
    return render(request, 'public/about.html')

def fellowships(request):
    """ A view to return the Fellowships page """
    return render(request, 'public/fellowships.html')

def mentoring(request):
    """ A view to return the Mentoring page """
    return render(request, 'public/mentoring.html')

def events(request):
    """ A view to return the Events page """
    return render(request, 'public/events.html')

def contact(request):
    """
    Renders an email form that allows users to send an inquiry
    to the WIFT organization
    """
    contact_form = ContactForm()
    context = {}
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()

            messages.success(
                request,
                "Thank you for your message. Someone from our team with contact you shortly.",
            )
            
            return redirect("contact")

        else:
            messages.error(request, "There is an error in the form.")
            return render(request, "public/contact.html", context)

    context = {
        "contact_form": contact_form,
    }

    return render(request, "public/contact.html", context)

def join(request):
    """ A view to return the Join page """
    form = RegistrationForm()
    context = {}
    
    categories = MembershipCategory.objects.all()
    context = {
        'form': form,
        'categories': categories,
    }
    
    return render(request, 'public/join.html', context)

def privacy_policy(request):
    """ A view to return the Privacy Policy page """
    return render(request, 'public/privacy_policy.html')