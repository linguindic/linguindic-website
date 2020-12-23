from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from django.db.models.functions import Lower
from .. import models


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
