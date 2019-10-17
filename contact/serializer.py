from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class ContactSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'



class NewsletterSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = '__all__'

