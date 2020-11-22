from rest_framework import serializers
from . import models


class LinguisticNotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LinguisticNotion
        fields = '__all__'
