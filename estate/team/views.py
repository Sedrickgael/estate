from django.shortcuts import render
from config.models import *
from construction.models import *
from .models import *
from django.db.models import Q
from datetime import date


# Create your views here.
def about(request):
    context={
        'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="About"'),
        'experiences':  APropos.objects.raw('SELECT id, date("now") - date( team_apropos.annee_creation) as annee FROM team_apropos'),
        'sociallinks':  SocialLink.objects.all().order_by('?')[:5],
        'identites':  Identite.objects.all()[:1],
        'bureau_count': Bureau.objects.all().count(),
        'plainte_count': Plainte.objects.all().count(),
        'house_count': House.objects.all().count(),
        'villa_counts': House.objects.raw('SELECT construction_house.id, COUNT(*) as count FROM construction_typedemaison, construction_house WHERE construction_house.type_maison_id=construction_typedemaison.id AND construction_typedemaison.types ="Villa basse"'),
        'abouts':  APropos.objects.all()[:1],
        'membres':  Membre.objects.all()[:4],
        'otherpages':  OtherPage.objects.all(),
        'slides':  AboutSlide.objects.all(),
        'pages':  Page.objects.filter(Q(nom='Contact') | Q(nom='About')),
        
    }
    return render(request,"estate/about.html", context)


