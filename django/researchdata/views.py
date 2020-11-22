from django.views.generic import (ListView, DetailView, TemplateView)
from rest_framework.generics import (RetrieveAPIView, ListAPIView)
from . import models, serializers


class LinguisticNotionListView(ListView):
    """
    Class-based view to show the linguistic notion list template
    """

    template_name = 'researchdata/linguisticnotion-list.html'
    model = models.LinguisticNotion
    paginate_by = 13


class LinguisticNotionDetailView(DetailView):
    """
    Class-based view to show the linguistic notion detail template
    """

    template_name = 'researchdata/linguisticnotion-detail.html'
    model = models.LinguisticNotion


# API views


class APITemplateView(TemplateView):
    """
    Display the API template
    """
    template_name = 'researchdata/api.html'


class LinguisticNotionListAPIView(ListAPIView):
    """
    Return list of all linguistic notions
    """
    queryset = models.LinguisticNotion.objects.all()
    serializer_class = serializers.LinguisticNotionSerializer


class LinguisticNotionRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific linguistic notion
    """
    queryset = models.LinguisticNotion.objects.all()
    serializer_class = serializers.LinguisticNotionSerializer
