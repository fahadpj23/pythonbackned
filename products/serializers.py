
from .models import cover
from rest_framework import serializers

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = cover
        fields = '__all__'