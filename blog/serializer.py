from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class CommentaireSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'


class NewVideoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = NewVideo
        fields = '__all__'


class NewImageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = NewImage
        fields = '__all__'


class NewSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    article_image = NewImageSerializer(many=True,  read_only=True, required=False )

    video_article = NewVideoSerializer(many=True,  read_only=True, required=False)
    
    commentaire_article = CommentaireSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = New
        fields = '__all__'

class AuteurSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    ecrit_par = NewSerializer(many=True,  read_only=True, required=False)


    class Meta:
        model = Auteur
        fields = '__all__'


class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    categorie_article = NewSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = Categorie
        fields = '__all__'