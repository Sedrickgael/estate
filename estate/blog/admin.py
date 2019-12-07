# Register your models here.
# vim: set fileencoding=utf-8 :

from django.contrib import admin



from . import models





class CategorieAdmin(admin.ModelAdmin):



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





class AuteurAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'date_add',

        'date_update',

        'status',

        'id',

        'date_add',

        'date_update',

        'status',

    )





class NewAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'tag',

        'description',

        'titre',

        'extrait',

        'header_image',

        'categorie',

        'auteur',

        'date_add',

        'date_update',

        'status',

        'slug',

    )

    list_filter = (

        'categorie',

        'auteur',

        'date_add',

        'date_update',

        'status',

        'id',

        'tag',

        'description',

        'titre',

        'extrait',

        'header_image',

        'categorie',

        'auteur',

        'date_add',

        'date_update',

        'status',

        'slug',

    )





class NewImageAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'image',

        'description',

        'article_image',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'article_image',

        'date_add',

        'date_update',

        'status',

        'id',

        'image',

        'description',

        'article_image',

        'date_add',

        'date_update',

        'status',

    )





class NewVideoAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'Video_url',

        'description',

        'article_video',

        'date_add',

        'date_update',

        'status',

    )

    list_filter = (

        'article_video',

        'date_add',

        'date_update',

        'status',

        'id',

        'Video_url',

        'description',

        'article_video',

        'date_add',

        'date_update',

        'status',

    )





class CommentaireAdmin(admin.ModelAdmin):



    list_display = (

        'id',

        'nom',

        'prenoms',

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

        'date_add',

        'date_update',

        'status',

    )





def _register(model, admin_class):

    admin.site.register(model, admin_class)





_register(models.Categorie, CategorieAdmin)

_register(models.Auteur, AuteurAdmin)

_register(models.New, NewAdmin)

_register(models.NewImage, NewImageAdmin)

_register(models.NewVideo, NewVideoAdmin)

_register(models.Commentaire, CommentaireAdmin)

