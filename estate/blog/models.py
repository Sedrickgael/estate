from django.db import models
from tinymce import HTMLField
from team.models import Membre


# Create your models here.
class Categorie(models.Model):
    """Model definition for Categorie."""

    nom = models.CharField( max_length=50)
    description = models.TextField()
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom


class Auteur(models.Model):
    """Model definition for Auteur."""

    membre=models.ForeignKey(Membre, related_name='auteur', on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Auteur."""

        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'
    def __str__(self):
        """Unicode representation of Categorie."""
        return self.membre.nom + ' '+ self.membre.prenoms


class New(models.Model):
    """Model definition for New."""

    titre = models.CharField( max_length=50)
    tag = models.CharField( max_length=50)
    description = models.TextField()
    titre = models.CharField( max_length=50)
    extrait = models.TextField()
    contenu = HTMLField('contenu')
    header_image = models.ImageField(upload_to='blog/articles/header_img/%Y/%m/%d/')
    categorie=models.ForeignKey(Categorie, related_name="categorie_article", on_delete=models.CASCADE)
    auteur=models.ForeignKey(Auteur, related_name="ecrit_par", on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    slug = models.SlugField()
    

    class Meta:
        """Meta definition for New."""

        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        """Unicode representation of New."""
        return self.titre


class NewImage(models.Model):
    """Model definition for NewImg."""

    image = models.ImageField(upload_to='blog/articles/images')
    description = models.TextField()
    article_image=models.ForeignKey(New, related_name='article_image', on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for NewImg."""

        verbose_name = 'NewImg'
        verbose_name_plural = 'NewImgs'

    def __str__(self):
        """Unicode representation of NewImg."""
        return self.description

class NewVideo(models.Model):
    """Model definition for NewVideo."""

    Video_url = models.URLField()
    description = models.TextField()
    article_video=models.ForeignKey(New, related_name='video_article', on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for NewVideo."""

        verbose_name = 'NewVideo'
        verbose_name_plural = 'NewVideo'

    def __str__(self):
        """Unicode representation of NewVideo."""
        return self.Video_url


class Commentaire(models.Model):
    """Model definition for Commentaire."""

    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    prenoms = models.CharField( max_length=100)
    commentaire:models.TextField()
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    new=models.ForeignKey(New, related_name='commentaire_article', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.nom + ' ' + self.prenoms


