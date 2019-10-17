from config.models import *
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def contact(request):
    context={
        'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="Contact"'),
        'sociallinks':  SocialLink.objects.all().order_by('?')[:5],
        'identites':  Identite.objects.all()[:1],
        'otherpages':  OtherPage.objects.all(),
        'pages':  Page.objects.filter(Q(nom='Contact') | Q(nom='About')),
    }
    return render(request,"estate/contact.html", context)



def postform(request):
    nom_complet = request.POST.get('nom_complet')
    sujet = request.POST.get('sujet')
    email = request.POST.get('email')
    message = request.POST.get('message')
    phone = request.POST.get('phone')
    
    issucces = False
    
    if nom_complet !='' and not nom_complet.isspace() and sujet != '' and not sujet.isspace() and message != '' and not message.isspace() and email != '' and not email.isspace() and phone != '' and not phone.isspace():
        issucces = True
        h = Contact(nom_complet=nom_complet,sujet=sujet,message=message,email=email,contact=phone)
        h.save()
        print(nom_complet,sujet,contact,email,message)
    else:
        issucces = False
    datas = {
        'succes': issucces,
        'name': nom_complet,
    }
    return JsonResponse(datas, safe=False)


def souscrire(request):
    email = request.POST.get('email')

    issucces = False
    
    if email != '' and not email.isspace() :
        issucces = True
        h = Newsletter(email=email)
        h.save()
        print(email)
    else:
        issucces = False
    datas = {
        'succes': issucces,
        'name': email,
    }
    return JsonResponse(datas, safe=False)

