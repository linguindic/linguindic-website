from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from django.db.models.functions import Lower
from .. import models


class BrowseReferenceDetailView(DetailView):
    """
    Class-based view to show the reference detail template
    """
    template_name = 'researchdata/browse-reference-detail.html'
    model = models.Reference


class BrowseReferenceListView(ListView):
    """
    Class-based view to show the reference list template
    """
    template_name = 'researchdata/browse-reference-list.html'
    model = models.Reference
    paginate_by = 30
