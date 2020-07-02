from rest_framework import viewsets
from .models import ListaNavbar
from .serializer import ListaNavbarSerializers


class ListaNavbarViewSet(viewsets.ModelViewSet):
    queryset = ListaNavbar.objects.all()
    serializer_class = ListaNavbarSerializers
