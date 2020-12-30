from django.views.generic import TemplateView
from rest_framework.generics import (RetrieveAPIView, ListAPIView)
from .. import models, serializers


class APITemplateView(TemplateView):
    """
    Display the API template
    """
    template_name = 'researchdata/api.html'


# Select List models


class SlLinguisticTraditionGroupListAPIView(ListAPIView):
    """
    Return list of all SlLinguisticTraditionGroup
    """
    queryset = models.SlLinguisticTraditionGroup.objects.all()
    serializer_class = serializers.SlLinguisticTraditionGroupSerializer


class SlLinguisticTraditionGroupRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific SlLinguisticTraditionGroup
    """
    queryset = models.SlLinguisticTraditionGroup.objects.all()
    serializer_class = serializers.SlLinguisticTraditionGroupSerializer


class SlLinguisticTraditionListAPIView(ListAPIView):
    """
    Return list of all SlLinguisticTradition
    """
    queryset = models.SlLinguisticTradition.objects.all()
    serializer_class = serializers.SlLinguisticTraditionSerializer


class SlLinguisticTraditionRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific SlLinguisticTradition
    """
    queryset = models.SlLinguisticTradition.objects.all()
    serializer_class = serializers.SlLinguisticTraditionSerializer


class SlReferencePublisherListAPIView(ListAPIView):
    """
    Return list of all SlReferencePublisher
    """
    queryset = models.SlReferencePublisher.objects.all()
    serializer_class = serializers.SlReferencePublisherSerializer


class SlReferencePublisherRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific SlReferencePublisher
    """
    queryset = models.SlReferencePublisher.objects.all()
    serializer_class = serializers.SlReferencePublisherSerializer


class SlReferenceTypeListAPIView(ListAPIView):
    """
    Return list of all SlReferenceType
    """
    queryset = models.SlReferenceType.objects.all()
    serializer_class = serializers.SlReferenceTypeSerializer


class SlReferenceTypeRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific SlReferenceType
    """
    queryset = models.SlReferenceType.objects.all()
    serializer_class = serializers.SlReferenceTypeSerializer


class SlTextGroupListAPIView(ListAPIView):
    """
    Return list of all SlTextGroup
    """
    queryset = models.SlTextGroup.objects.all()
    serializer_class = serializers.SlTextGroupSerializer


class SlTextGroupRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific SlTextGroup
    """
    queryset = models.SlTextGroup.objects.all()
    serializer_class = serializers.SlTextGroupSerializer


class SlTextTypeListAPIView(ListAPIView):
    """
    Return list of all SlTextType
    """
    queryset = models.SlTextType.objects.all()
    serializer_class = serializers.SlTextTypeSerializer


class SlTextTypeRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific SlTextType
    """
    queryset = models.SlTextType.objects.all()
    serializer_class = serializers.SlTextTypeSerializer


# Main models


class ReferenceListAPIView(ListAPIView):
    """
    Return list of all Reference
    """
    queryset = models.Reference.objects.all()
    serializer_class = serializers.ReferenceSerializer


class ReferenceRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific Reference
    """
    queryset = models.Reference.objects.all()
    serializer_class = serializers.ReferenceSerializer


class TextListAPIView(ListAPIView):
    """
    Return list of all Text
    """
    queryset = models.Text.objects.all()
    serializer_class = serializers.TextSerializer


class TextRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific Text
    """
    queryset = models.Text.objects.all()
    serializer_class = serializers.TextSerializer


class AuthorListAPIView(ListAPIView):
    """
    Return list of all Author
    """
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific Author
    """
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class LinguisticFieldListAPIView(ListAPIView):
    """
    Return list of all LinguisticField
    """
    queryset = models.LinguisticField.objects.all()
    serializer_class = serializers.LinguisticFieldSerializer


class LinguisticFieldRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific LinguisticField
    """
    queryset = models.LinguisticField.objects.all()
    serializer_class = serializers.LinguisticFieldSerializer


class LinguisticNotionListAPIView(ListAPIView):
    """
    Return list of all LinguisticNotion
    """
    queryset = models.LinguisticNotion.objects.all()
    serializer_class = serializers.LinguisticNotionSerializer


class LinguisticNotionRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific LinguisticNotion
    """
    queryset = models.LinguisticNotion.objects.all()
    serializer_class = serializers.LinguisticNotionSerializer
