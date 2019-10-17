from django.db import models

# Create your models here.
class Contact(models.Model):
    """Model definition for Contact."""

    nom_complet = models.CharField( max_length=255)
    email = models.EmailField(max_length=254)
    sujet = models.CharField( max_length=50)
    message = models.TextField()
    contact = models.CharField(max_length=20)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)



    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.sujet



class Newsletter(models.Model):
    """Model definition for Newsletter."""

    email = models.EmailField(max_length=254)
    date_add = models.DateTimeField(  auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Newsletter."""

        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        """Unicode representation of Newsletter."""
        return self.email

