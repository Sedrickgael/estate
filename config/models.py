from django.db import models

# Create your models here.
class Identite(models.Model):
    """Model definition for Identite."""

    nom = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/config/')
    footer_logo = models.ImageField(upload_to='images/config/')
    maps_link = models.TextField()
    favicone = models.ImageField(upload_to='images/config/')
    newsletter_message=models.TextField()
    adresse=models.CharField(max_length=255)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    description = models.TextField()

    class Meta:
        """Meta definition for Identite."""

        verbose_name = 'Identite'
        verbose_name_plural = 'Identites'

    def __str__(self):
        """Unicode representation of Identite."""
        return self.nom

class Bureau(models.Model):
    """Model definition for Bureau."""

    maps_link = models.URLField()
    adresse=models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/config/bureau/')
    contact = models.CharField(max_length=50)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Bureau."""

        verbose_name = 'Bureau'
        verbose_name_plural = 'Bureaus'

    def __str__(self):
        """Unicode representation of Bureau."""
        return self.adresse

class Consultant(models.Model):
    """Model definition for Consultant."""

    nom = models.CharField( max_length=50)
    prenoms = models.CharField( max_length=50)
    image = models.ImageField(upload_to='images/config/bureau/')
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Consultant."""

        verbose_name = 'Consultant'
        verbose_name_plural = 'Consultants'

    def __str__(self):
        """Unicode representation of Consultant."""
        return self.nom

class Plainte(models.Model):
    """Model definition for Plainte."""

    nom = models.CharField( max_length=50)
    prenoms = models.CharField( max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    cause = models.CharField(max_length=50)
    message = models.TextField()
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    

    class Meta:
        """Meta definition for Plainte."""

        verbose_name = 'Plainte'
        verbose_name_plural = 'Plaintes'

    def __str__(self):
        """Unicode representation of Plainte."""
        return self.cause


class Page(models.Model):
    """Model definition for Page."""

    nom = models.CharField( max_length=50)
    titre = models.CharField( max_length=50)
    link = models.CharField( max_length=50)
    description = models.CharField(max_length=50)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Page."""

        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        """Unicode representation of Page."""
        return self.titre


class OtherPage(models.Model):
    """Model definition for OtherPage."""

    nom = models.CharField( max_length=50)
    titre = models.CharField( max_length=50)
    link = models.CharField( max_length=50)
    description = models.CharField(max_length=50)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for OtherPage."""

        verbose_name = 'OtherPage'
        verbose_name_plural = 'OtherPages'

    def __str__(self):
        """Unicode representation of OtherPage."""
        return self.titre

class HeaderSlide(models.Model):
    """Model definition for HeaderSlide."""

    image = models.ImageField(upload_to='images/config/header/')
    description = models.CharField( max_length=50)
    page= models.ForeignKey(Page, related_name='page', on_delete=models.CASCADE)
    sous_titre=models.CharField(max_length=50, null=True)
    sous_description = models.TextField(null=True)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for HeaderSlide."""

        verbose_name = 'HeaderSlide'
        verbose_name_plural = 'HeaderSlides'

    def __str__(self):
        """Unicode representation of HeaderSlide."""
        return self.description



class Header(models.Model):
    """Model definition for Header."""

    image = models.ImageField(upload_to='images/config/header/')
    description = models.CharField( max_length=50)
    page= models.ForeignKey(OtherPage, related_name='page', on_delete=models.CASCADE)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Header."""

        verbose_name = 'Header'
        verbose_name_plural = 'Headers'

    def __str__(self):
        """Unicode representation of Header."""
        return self.description

class SocialLink(models.Model):
    """Model definition for SocialLink."""

    nom = models.CharField( max_length=50)
    lien = models.URLField()
    icone_classe = models.CharField(max_length=50, null=True)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for SocialLink."""

        verbose_name = 'SocialLink'
        verbose_name_plural = 'SocialLinks'

    def __str__(self):
        """Unicode representation of SocialLink."""
        return self.nom

class Caracteristique(models.Model):
    """Model definition for Caracteristique."""

    nom = models.CharField(max_length=50)
    description = models.TextField()
    icone_classe = models.CharField(max_length=50)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Caracteristique."""

        verbose_name = 'Caracteristique'
        verbose_name_plural = 'Caracteristiques'

    def __str__(self):
        """Unicode representation of Caracteristique."""
        return self.nom

