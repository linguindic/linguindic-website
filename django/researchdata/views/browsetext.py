from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from django.db.models.functions import Lower
from .. import models


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
