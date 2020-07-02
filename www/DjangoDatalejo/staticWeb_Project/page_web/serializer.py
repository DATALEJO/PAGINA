from .models import ListaNavbar, Articulo
from rest_framework import serializers


class ListaNavbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListaNavbar
        fields = '__all__'
