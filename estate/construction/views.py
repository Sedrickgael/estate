from django.shortcuts import render
from .models import *
from config.models import *
from django.db.models import Q

# Create your views here.
def index(request):
    context={
        'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="Accueil"'),
        'sociallinks':  SocialLink.objects.all().order_by('?')[:5],
        'localistations':  Localisation.objects.all().order_by('?')[:1],
        'consultants':  Consultant.objects.all().order_by('?')[:1],
        'interieurs':  Image_interieur.objects.all()[:5],
        'houses': House.objects.all().order_by('?')[:2],
        'identites':  Identite.objects.all()[:1],
        'otherpages':  OtherPage.objects.all(),
        'pages':  Page.objects.filter(Q(nom='Contact') | Q(nom='About')),
        'caracteristiques':  Caracteristique.objects.all().order_by('?')[:9],
        'traits':  Caracteristique.objects.all().order_by('?')[:5],
    }

    return render(request,"estate/index.html", context)


def housedetails(request, slug):
    context={
        'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="HouseDetails"'),
        'interieurs':  Image_interieur.objects.raw('SELECT * FROM construction_house, construction_image_interieur WHERE construction_image_interieur.house_id=construction_house.id AND construction_house.slug = %s', [slug]),
        'identites':  Identite.objects.all()[:1],
        'consultants':  Consultant.objects.all().order_by('?')[:1],
        'commodites':  Commodite.objects.raw('SELECT * FROM construction_house, construction_commodite WHERE construction_commodite.house_id=construction_house.id AND construction_house.slug = %s', [slug]),
        'sociallinks':  SocialLink.objects.all().order_by('?')[:5],
        'otherpages':  OtherPage.objects.all().order_by('?')[:3],
        'pages':  Page.objects.filter(Q(nom='Contact') | Q(nom='About')),
        'houses': House.objects.filter(slug=slug),
        'caracteristiques':  Caracteristique.objects.all().order_by('?')[:5],

    }
    return render(request,"estate/property.html", context)


def house(request):

    context={
        'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="nos maisons"'),
        'identites':  Identite.objects.all()[:1],
        'commodites':  Commodite.objects.all(),
        'sociallinks':  SocialLink.objects.all().order_by('?')[:5],
        'otherpages':  OtherPage.objects.all().order_by('?')[:3],
        'pages':  Page.objects.filter(Q(nom='Contact') | Q(nom='About')),
        'caracteristiques':  Caracteristique.objects.all(),
        'houses': House.objects.all().order_by('?'),
    }
    return render(request,"estate/developpements.html", context)

