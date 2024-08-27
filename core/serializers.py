from rest_framework import serializers
from .models import Sonho

class SonhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sonho
        fields = '__all__'
