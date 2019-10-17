from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :

from django.contrib import admin



from . import models





class ContactAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom_complet',

        'email',

        'contact',

        'sujet',

        'message',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'contact',
        
        'date_add',

        'date_update',

        'status',

        'id',

        'nom_complet',

        'email',

        'sujet',

        'message',

        'date_add',

        'date_update',

        'status',

    )





class NewsletterAdmin(admin.ModelAdmin):



    list_display = ('id', 'email', 'date_add', 'date_update', 'status')

    list_filter = (

        'date_add',

        'date_update',

        'status',

        'id',

        'email',

        'date_add',

        'date_update',

        'status',

    )





def _register(model, admin_class):

    admin.site.register(model, admin_class)





_register(models.Contact, ContactAdmin)

_register(models.Newsletter, NewsletterAdmin)

