from django.shortcuts import render
from membership.models import MembershipCategory
from membership.forms import MembershipLevelSelectionForm

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
    """ A view to return the Contact page """
    return render(request, 'public/contact.html')

def join(request):
    """ A view to return the Join page """
    form = MembershipLevelSelectionForm()
    membership_level = MembershipCategory.objects.all()
    
    context = {
        'membership_level': membership_level,
        'form': form,
    }

    return render(request, 'public/join.html', context)