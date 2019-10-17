from django.db import models
from config.models import Bureau
from datetime import date

# Create your models here.

class Poste(models.Model):
    """Model definition for Post."""

    nom = models.CharField(max_length=50)
    description = models.TextField()
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return 


class Membre(models.Model):
    """Model definition for Membre."""

    nom = models.CharField( max_length=50)
    prenoms = models.CharField( max_length=255)
    poste = models.ForeignKey(Poste, related_name='poste', on_delete=models.CASCADE)
    bureau = models.ForeignKey(Bureau, related_name='agent', on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField( upload_to='images/about/team/')
    contact = models.CharField( max_length=50)
    adresse = models.CharField( max_length=255)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)


    class Meta:
        """Meta definition for Membre."""

        verbose_name = 'Membre'
        verbose_name_plural = 'Membres'

    def __str__(self):
        """Unicode representation of Membre."""
        return self.nom + ' ' + self.prenoms

class APropos(models.Model):
    """Model definition for APropos."""

    nom_entreprise=models.CharField(max_length=50)
    description = models.TextField()
    annee_creation = models.DateField(null=True)
    join_team_message = models.TextField()
    work_remote = models.TextField()
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)


    class Meta:
        """Meta definition for APropos."""

        verbose_name = 'APropos'
        verbose_name_plural = 'AProposs'

    def __str__(self):
        """Unicode representation of APropos."""
        return self.nom_entreprise

    def experience(self):
        return int(date.today) - int(self.annee_creation)

class AboutSlide(models.Model):
    """Model definition for AboutSlide."""

    image = models.ImageField(upload_to='images/team/about/')
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for AboutSlide."""

        verbose_name = 'AboutSlide'
        verbose_name_plural = 'AboutSlides'

    