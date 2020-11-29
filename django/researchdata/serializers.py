from rest_framework import serializers
from . import models


# Select List models

class SlLinguisticNotionsRelationshipTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlLinguisticNotionsRelationshipType
        fields = '__all__'


class SlLinguisticTraditionGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlLinguisticTraditionGroup
        fields = '__all__'


class SlLinguisticTraditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SlLinguisticTradition
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

class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reference
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Text
        fields = '__all__'


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


# Many to Many models

class M2MLinguisticNotionsRelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.M2MLinguisticNotionsRelationship
        fields = '__all__'
