from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *
from team.serializer import MembreSerializer


class CaracteristiqueSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Caracteristique
        fields = '__all__'



class SocialLinkSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = SocialLink
        fields = '__all__'




class HeaderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

  
    class Meta:
        model = Header
        fields = '__all__'


class HeaderSlideSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = HeaderSlide
        fields = '__all__'


class OtherPageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    page = HeaderSerializer(many=True,  read_only=True, required=False)


    class Meta:
        model = OtherPage
        fields = '__all__'


class PageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    page = HeaderSlideSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = Page
        fields = '__all__'

class PlainteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Plainte
        fields = '__all__'

class ConsultantSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Consultant
        fields = '__all__'

class IdentiteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Identite
        fields = '__all__'

class BureauSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    agent = MembreSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = Bureau
        fields = '__all__'