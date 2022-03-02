from .models import anuncio,calendario
from rest_framework import serializers


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model=anuncio
        fields = '__all__'


class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=calendario
        fields = '__all__'