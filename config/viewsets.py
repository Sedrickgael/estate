from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class CaracteristiqueViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Caracteristique.objects.all()
    serializer_class = CaracteristiqueSerializer


class SocialLinkViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class HeaderViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class HeaderSlideViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = HeaderSlide.objects.all()
    serializer_class = HeaderSlideSerializer


class OtherPageViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = OtherPage.objects.all()
    serializer_class = OtherPageSerializer

class PageViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PlainteViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Plainte.objects.all()
    serializer_class = PlainteSerializer

class ConsultantViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

class IdentiteViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Identite.objects.all()
    serializer_class = IdentiteSerializer

class BureauViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Bureau.objects.all()
    serializer_class = BureauSerializer