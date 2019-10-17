from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class LocalisationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Localisation
        fields = '__all__'


class Image_interieurSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Image_interieur
        fields = '__all__'


class CommoditeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Commodite
        fields = '__all__'


class HouseSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    house_commodite = CommoditeSerializer(many=True,  read_only=True, required=False)
    house_image = Image_interieurSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = House
        fields = '__all__'


class TypeDeMaisonSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    type_de_maison = HouseSerializer(many=True,  read_only=True, required=False)


    class Meta:
        model = TypeDeMaison
        fields = '__all__'
