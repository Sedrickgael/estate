from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class LocalisationViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer


class Image_interieurViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Image_interieur.objects.filter(status=True)
    serializer_class = Image_interieurSerializer


class CommoditeViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Commodite.objects.filter(status=True)
    serializer_class = CommoditeSerializer


class HouseViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = House.objects.filter(status=True)
    serializer_class = HouseSerializer


class TypeDeMaisonViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = TypeDeMaison.objects.all()
    serializer_class = TypeDeMaisonSerializer

