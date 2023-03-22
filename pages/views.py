from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

# Create your views here.

def index(request):
    # ilk 3 kayıt [:3]
    listings = Listing.objects.order_by('-yayin_tarihi').filter(is_published = True) [:3]

    context = {
        'listings' : listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request,'pages/index.html', context)


def about(request):
    #GET ALL REALTORS
    realtors = Realtor.objects.order_by('-uyelik_tarihi')
    #GET MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request,'pages/about.html', context)