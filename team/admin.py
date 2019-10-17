from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :

from django.contrib import admin



from . import models





class PosteAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'description',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'date_add',

        'date_update',

        'status',

        'id',

        'nom',

        'description',

        'date_add',

        'date_update',

        'status',

    )





class MembreAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'prenoms',

        'poste',

        'bureau',

        'bio',

        'avatar',

        'contact',

        'adresse',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'poste',

        'bureau',

        'date_add',

        'date_update',

        'status',

        'id',

        'nom',

        'prenoms',

        'poste',

        'bureau',

        'bio',

        'avatar',

        'contact',

        'adresse',

        'date_add',

        'date_update',

        'status',

    )





class AProposAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom_entreprise',

        'description',

        'annee_creation',

        'join_team_message',

        'work_remote',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'date_add',

        'date_update',

        'status',

        'id',

        'nom_entreprise',

        'description',

        'annee_creation',

        'join_team_message',

        'work_remote',

        'date_add',

        'date_update',

        'status',

    )





class AboutSlideAdmin(admin.ModelAdmin):



    list_display = ('id', 'image', 'date_add', 'date_update', 'status')

    list_filter = (

        'date_add',

        'date_update',

        'status',

        'id',

        'image',

        'date_add',

        'date_update',

        'status',

    )





def _register(model, admin_class):

    admin.site.register(model, admin_class)





_register(models.Poste, PosteAdmin)

_register(models.Membre, MembreAdmin)

_register(models.APropos, AProposAdmin)

_register(models.AboutSlide, AboutSlideAdmin)

