from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class CommentaireViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer


class NewVideoViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = NewVideo.objects.all()
    serializer_class = NewVideoSerializer


class NewImageViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = NewImage.objects.all()
    serializer_class = NewImageSerializer


class NewViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = New.objects.all()
    serializer_class = NewSerializer


class AuteurViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer