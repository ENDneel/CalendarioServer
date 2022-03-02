from rest_framework import viewsets
from .models import anuncio,calendario
from .serializer import AnuncioSerializer,CalendarioSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = anuncio.objects.all()
    serializer_class = AnuncioSerializer
class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = calendario.objects.all()
    serializer_class = CalendarioSerializer