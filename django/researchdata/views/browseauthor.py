from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from django.db.models.functions import Lower
from .. import models


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
