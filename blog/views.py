from django.shortcuts import render
from config.models import *
from team.models import *
from django.http import JsonResponse
import json
from .models import *
from django.db.models import Q

# Create your views here.
def blog(request):
    context={
        'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="New"'),
        'allnews':  New.objects.all(),
        # 'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="New"'),
        # 'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="New"'),
        # 'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="New"'),
        'sociallinks':  SocialLink.objects.all().order_by('?')[:5],
        'categories':  Categorie.objects.all()[:4],
        'consultants':  Consultant.objects.all().order_by('?')[:1],
        'identites':  Identite.objects.all()[:1],
        'otherpages':  OtherPage.objects.all(),
        'pages':  Page.objects.filter(Q(nom='Contact') | Q(nom='About')),
       
    }

    return render(request,"estate/blog.html", context)




def blogdetails(request, slug):
    context={
        'headerslides':  HeaderSlide.objects.raw('SELECT * FROM config_headerslide, config_page WHERE config_headerslide.page_id=config_page.id AND config_page.nom ="BlogDetails"'),
        'sociallinks':  SocialLink.objects.all().order_by('?')[:5],
        'identites':  Identite.objects.all()[:1],
        'otherpages':  OtherPage.objects.all(),
        'news':  New.objects.filter(slug=slug),
        'commentaires':  Commentaire.objects.all(),
        'images':  NewImage.objects.raw('SELECT * FROM blog_newimage, blog_new WHERE blog_newimage.article_image_id=blog_new.id AND blog_new.slug = %s', [slug]),
        'videos':  NewVideo.objects.raw('SELECT * FROM blog_newvideo, blog_new WHERE blog_newvideo.article_video_id=blog_new.id AND blog_new.slug = %s', [slug]),
        'pages':  Page.objects.filter(Q(nom='Contact') | Q(nom='About')),
    }

    return render(request,"estate/newdetail.html", context)


def comment(request, id):
    nom = request.POST.get('nom_complet')
    prenoms = request.POST.get('sujet')
    email = request.POST.get('email')
    commentaire = request.POST.get('message')
    id = id
    
    issucces = False
    
    if nom !='' and not nom.isspace() and prenoms != '' and not prenoms.isspace() and commentaire != '' and not commentaire.isspace() and email != '' and not email.isspace():
        issucces = True
        h = Commentaire(nom=nom,prenoms=prenoms,commentaire=commentaire,email=email, news=id)
        h.save()
        print(nom,prenoms,email,commentaire,id)
    else:
        issucces = False
    datas = {
        'succes': issucces,
        'name': nom,
    }
    return JsonResponse(datas, safe=False)