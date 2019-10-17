from django.db import models

# Create your models here.

class TypeDeMaison(models.Model):
    """Model definition for TypeDeMaison."""

    types = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)


    class Meta:
        """Meta definition for TypeDeMaison."""

        verbose_name = 'TypeDeMaison'
        verbose_name_plural = 'TypeDeMaisons'

    def __str__(self):
        """Unicode representation of TypeDeMaison."""
        return self.types

class House(models.Model):
    """Model definition for House."""

    description = models.TextField()
    image_preview = models.ImageField(upload_to='images/construction/previews/')
    image_fascade = models.ImageField(upload_to='images/construction/fascade/')
    preview_text = models.TextField()
    adresse = models.CharField(max_length=255)
    prix = models.PositiveIntegerField()
    taille_lot=models.PositiveIntegerField()
    type_maison=models.ForeignKey(TypeDeMaison, related_name='type_de_maison', on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    est_termine = models.BooleanField(default=True)
    status=models.BooleanField(default=True)
    slug = models.SlugField()



    class Meta:
        """Meta definition for House."""

        verbose_name = 'House'
        verbose_name_plural = 'Houses'

    def __str__(self):
        """Unicode representation of House."""
        return self.adresse + ' '+self.description

class Localisation(models.Model):
    """Model definition for Localisation."""

    allentour = models.ImageField(upload_to='images/construction/localisation')
    interieur = models.ImageField(upload_to='images/construction/localisation')
    piscine = models.ImageField(upload_to='images/construction/localisation')
    vue = models.ImageField(upload_to='images/construction/localisation')
    video_allentour = models.URLField()
    video_interieur = models.URLField()
    video_oiscine = models.URLField()
    video_vue = models.URLField()
    interieur_description = models.TextField()
    environnement_description = models.TextField()
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    
    class Meta:
        """Meta definition for Localisation."""

        verbose_name = 'Localisation'
        verbose_name_plural = 'Localisations'

    def __str__(self):
        """Unicode representation of Localisation."""
        return self.environnement_description



class Commodite(models.Model):
    """Model definition for Commodite."""

    nom=models.CharField(max_length=100)
    quantite=models.PositiveIntegerField()
    description = models.TextField()
    icone_commodite = models.CharField(max_length=70)
    house=models.ForeignKey(House, related_name='house_commodite', on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Commodite."""

        verbose_name = 'Commodite'
        verbose_name_plural = 'Commodites'

    def __str__(self):
        """Unicode representation of Commodite."""
        return self.nom


class Image_interieur(models.Model):
    """Model definition for Image_interieur."""

    description = models.TextField()
    image = models.ImageField(upload_to='images/construction/commodite/', null=True)
    house=models.ForeignKey(House, related_name='house_image', on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Image_interieur."""

        verbose_name = 'Image_interieur'
        verbose_name_plural = 'Image_interieur'

    def __str__(self):
        """Unicode representation of Commodite."""
        return self.description




