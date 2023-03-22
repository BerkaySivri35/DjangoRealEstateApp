from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator
from listings.choices import bedroom_choices, price_choices, state_choices

# Create your views here.

def index(request):
    #Hapsini gösterme
    #listings = Listing.objects.all()

    #Tarihe göre sıralama
    listings = Listing.objects.order_by('-yayin_tarihi').filter(is_published = True)

    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings' : paged_listings
        
    }
    return render(request, 'listings/listings.html',context)


def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    #getting internal photos
    internal_photos = []
    for i in range(1, 6):
        if getattr(listing, 'photo_%d' %i):
            photo = getattr(listing, 'photo_%d' %i)
            internal_photos.append(photo)
 
    context = {
        'listing': listing,
        'internal_photos': internal_photos
    }
    # context = {
    #      'listing':listing
    # }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-yayin_tarihi')

    #form field names keywords,city,state,bedrooms,price
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(aciklama__icontains=keywords)
    
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(il__iexact = state)
    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(ilce__iexact = city)
    
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(yatak_odasi__lte = bedrooms)
            #lte = less than equals.
    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(fiyat__lte = price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)