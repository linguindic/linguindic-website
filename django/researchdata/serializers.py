from rest_framework import serializers
from . import models


# Select List models


class SlLinguisticTraditionGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlLinguisticTraditionGroup
        fields = '__all__'


class SlReferencePublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlReferencePublisher
        fields = '__all__'


class SlReferenceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlReferenceType
        fields = '__all__'


class SlTextGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlTextGroup
        fields = '__all__'


class SlTextTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlTextType
        fields = '__all__'


# Main models


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = '__all__'


class LinguisticFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LinguisticField
        fields = '__all__'


class LinguisticNotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LinguisticNotion
        fields = '__all__'


class LinguisticTraditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LinguisticTradition
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reference
        fields = '__all__'


class SanskritWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SanskritWord
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Text
        fields = '__all__'
