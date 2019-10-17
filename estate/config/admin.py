from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :

from django.contrib import admin



from . import models





class IdentiteAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'logo',

        'maps_link',

        'favicone',

        'newsletter_message',

        'adresse',

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

        'logo',

        'maps_link',

        'favicone',

        'newsletter_message',

        'adresse',

        'date_add',

        'date_update',

        'status',

    )





class BureauAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'maps_link',

        'adresse',

        'image',

        'contact',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'date_add',

        'date_update',

        'status',

        'id',

        'maps_link',

        'adresse',

        'image',

        'contact',

        'date_add',

        'date_update',

        'status',

    )





class ConsultantAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'prenoms',

        'image',

        'contact',

        'email',

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

        'prenoms',

        'image',

        'contact',

        'email',

        'date_add',

        'date_update',

        'status',

    )





class PlainteAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'prenoms',

        'contact',

        'email',

        'cause',

        'message',

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

        'prenoms',

        'contact',

        'email',

        'cause',

        'message',

        'date_add',

        'date_update',

        'status',

    )





class PageAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'titre',

        'link',

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

        'titre',

        'link',

        'description',

        'date_add',

        'date_update',

        'status',

    )





class OtherPageAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'titre',

        'link',

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

        'titre',

        'link',

        'description',

        'date_add',

        'date_update',

        'status',

    )





class HeaderSlideAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'image',

        'description',

        'page',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'page',

        'date_add',

        'date_update',

        'status',

        'id',

        'image',

        'description',

        'page',

        'date_add',

        'date_update',

        'status',

    )





class HeaderAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'image',

        'description',

        'page',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'page',

        'date_add',

        'date_update',

        'status',

        'id',

        'image',

        'description',

        'page',

        'date_add',

        'date_update',

        'status',

    )





class SocialLinkAdmin(admin.ModelAdmin):



    list_display = ('id', 'icone_classe', 'nom', 'lien', 'date_add', 'date_update', 'status')

    list_filter = (

        'date_add',

        'date_update',

        'icone_classe',

        'status',

        'id',

        'nom',

        'lien',

        'date_add',

        'date_update',

        'status',

    )





class CaracteristiqueAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'description',

        'icone_classe',

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

        'icone_classe',

        'date_add',

        'date_update',

        'status',

    )





def _register(model, admin_class):

    admin.site.register(model, admin_class)





_register(models.Identite, IdentiteAdmin)

_register(models.Bureau, BureauAdmin)

_register(models.Consultant, ConsultantAdmin)

_register(models.Plainte, PlainteAdmin)

_register(models.Page, PageAdmin)

_register(models.OtherPage, OtherPageAdmin)

_register(models.HeaderSlide, HeaderSlideAdmin)

_register(models.Header, HeaderAdmin)

_register(models.SocialLink, SocialLinkAdmin)

_register(models.Caracteristique, CaracteristiqueAdmin)

