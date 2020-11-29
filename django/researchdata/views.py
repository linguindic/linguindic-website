from django.views.generic import (ListView, DetailView, TemplateView)
from rest_framework.generics import (RetrieveAPIView, ListAPIView)
from . import models, serializers


# *************
# Website views
# *************


class BrowseReferenceListView(ListView):
    """
    Class-based view to show the reference list template
    """
    template_name = 'researchdata/browse-reference-list.html'
    model = models.Reference
    paginate_by = 30


class BrowseReferenceDetailView(DetailView):
    """
    Class-based view to show the reference detail template
    """
    template_name = 'researchdata/browse-reference-detail.html'
    model = models.Reference


class BrowseTextListView(ListView):
    """
    Class-based view to show the text list template
    """
    template_name = 'researchdata/browse-text-list.html'
    model = models.Text
    paginate_by = 30


class BrowseTextDetailView(DetailView):
    """
    Class-based view to show the text detail template
    """
    template_name = 'researchdata/browse-text-detail.html'
    model = models.Text


class BrowseAuthorListView(ListView):
    """
    Class-based view to show the author list template
    """
    template_name = 'researchdata/browse-author-list.html'
    model = models.Author
    paginate_by = 30


class BrowseAuthorDetailView(DetailView):
    """
    Class-based view to show the author detail template
    """
    template_name = 'researchdata/browse-author-detail.html'
    model = models.Author


class BrowseLinguisticFieldListView(ListView):
    """
    Class-based view to show the linguistic field list template
    """
    template_name = 'researchdata/browse-linguisticfield-list.html'
    model = models.LinguisticField
    paginate_by = 30


class BrowseLinguisticFieldDetailView(DetailView):
    """
    Class-based view to show the linguistic field detail template
    """
    template_name = 'researchdata/browse-linguisticfield-detail.html'
    model = models.LinguisticField


class BrowseLinguisticNotionListView(ListView):
    """
    Class-based view to show the linguistic notion list template
    """
    template_name = 'researchdata/browse-linguisticnotion-list.html'
    model = models.LinguisticNotion
    paginate_by = 30


class BrowseLinguisticNotionDetailView(DetailView):
    """
    Class-based view to show the linguistic notion detail template
    """
    template_name = 'researchdata/browse-linguisticnotion-detail.html'
    model = models.LinguisticNotion


class CompareLinguisticNotionsTemplateView(TemplateView):
    """
    Class-based view to show the compare linguistic notions template
    """
    template_name = 'researchdata/compare-linguisticnotions.html'


class VisualiseTemplateView(TemplateView):
    """
    Class-based view to show the visualise template
    """
    template_name = 'researchdata/visualise.html'


# *********
# API views
# *********


class APITemplateView(TemplateView):
    """
    Display the API template
    """
    template_name = 'researchdata/api.html'


# Select List models


class SlLinguisticNotionsRelationshipTypeListAPIView(ListAPIView):
    """
    Return list of all SlLinguisticNotionsRelationshipType
    """
    queryset = models.SlLinguisticNotionsRelationshipType.objects.all()
    serializer_class = serializers.SlLinguisticNotionsRelationshipTypeSerializer


class SlLinguisticNotionsRelationshipTypeRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific SlLinguisticNotionsRelationshipType
    """
    queryset = models.SlLinguisticNotionsRelationshipType.objects.all()
    serializer_class = serializers.SlLinguisticNotionsRelationshipTypeSerializer


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


# Many to Many models

class M2MLinguisticNotionsRelationshipListAPIView(ListAPIView):
    """
    Return list of all M2MLinguisticNotionsRelationship
    """
    queryset = models.M2MLinguisticNotionsRelationship.objects.all()
    serializer_class = serializers.M2MLinguisticNotionsRelationshipSerializer


class M2MLinguisticNotionsRelationshipRetrieveAPIView(RetrieveAPIView):
    """
    Return a specific M2MLinguisticNotionsRelationship
    """
    queryset = models.M2MLinguisticNotionsRelationship.objects.all()
    serializer_class = serializers.M2MLinguisticNotionsRelationshipSerializer
