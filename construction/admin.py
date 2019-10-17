from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :

from django.contrib import admin



from . import models





class TypeDeMaisonAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'types',

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

        'types',

        'description',

        'date_add',

        'date_update',

        'status',

    )





class HouseAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'description',

        'image_preview',

        'preview_text',

        'adresse',

        'prix',

        'slug',

        'taille_lot',

        'type_maison',

        'date_add',

        'date_update',

        'est_termine',

        'status',

    )

    list_filter = (

        'type_maison',

        'date_add',

        'date_update',

        'est_termine',

        'status',

        'id',

        'description',

        'image_preview',

        'preview_text',

        'adresse',

        'prix',

        'slug',

        'taille_lot',

        'type_maison',

        'date_add',

        'date_update',

        'est_termine',

        'status',

    )





class LocalisationAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'allentour',

        'interieur',

        'piscine',

        'vue',

        'video_allentour',

        'video_interieur',

        'video_oiscine',

        'video_vue',

        'interieur_description',

        'environnement_description',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'date_add',

        'date_update',

        'status',

        'id',

        'allentour',

        'interieur',

        'piscine',

        'vue',

        'video_allentour',

        'video_interieur',

        'video_oiscine',

        'video_vue',

        'interieur_description',

        'environnement_description',

        'date_add',

        'date_update',

        'status',

    )





class CommoditeAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'quantite',

        'description',

        'icone_commodite',

        'house',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'house',

        'date_add',

        'date_update',

        'status',

        'id',

        'nom',

        'quantite',

        'description',

        'icone_commodite',

        'house',

        'date_add',

        'date_update',

        'status',

    )





class Image_interieurAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'description',

        'image',

        'house',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'house',

        'date_add',

        'date_update',

        'status',

        'id',

        'description',

        'image',

        'house',

        'date_add',

        'date_update',

        'status',

    )





def _register(model, admin_class):

    admin.site.register(model, admin_class)





_register(models.TypeDeMaison, TypeDeMaisonAdmin)

_register(models.House, HouseAdmin)

_register(models.Localisation, LocalisationAdmin)

_register(models.Commodite, CommoditeAdmin)

_register(models.Image_interieur, Image_interieurAdmin)

