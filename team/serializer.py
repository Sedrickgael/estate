from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *
from blog.serializer import AuteurSerializer


class MembreSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    auteur = AuteurSerializer(many=True,  read_only=True, required=False)


    class Meta:
        model = Membre
        fields = '__all__'



class PosteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    poste = MembreSerializer(many=True,  read_only=True)

   
    class Meta:
        model = Poste
        fields = '__all__'




