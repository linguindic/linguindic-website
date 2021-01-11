from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from django.db.models.functions import Lower
from .. import models


class BrowseLinguisticFieldDetailView(DetailView):
    """
    Class-based view to show the linguistic field detail template
    """
    template_name = 'researchdata/browse-linguisticfield-detail.html'
    model = models.LinguisticField


class BrowseLinguisticFieldListView(ListView):
    """
    Class-based view to show the linguistic field list template
    """
    template_name = 'researchdata/browse-linguisticfield-list.html'
    model = models.LinguisticField
    paginate_by = 30

    def get_queryset(self):
        """
        This view returns either all objects or, if provided, will restrict the returned data based on 'search', 'filter', and 'order' criteria
        """

        # Start with all objects, which may be filtered/ordered below if such data is included in the request
        queryset = self.model.objects.all()

        #
        # Search
        #

        search = self.request.GET.get('search', '')
        advanced_search_by = self.request.GET.get('advanced_search_by', '')
        advanced_search_criteria = self.request.GET.get('advanced_search_criteria', '')

        # Either use the simple search or 'advanced' search (if advanced search is for all fields)
        if search != '' or (advanced_search_by == '' and advanced_search_criteria != ''):

            # Work out if the simple search or advanced search is being provided
            search_val = search if advanced_search_criteria == '' else advanced_search_criteria

            queryset = queryset.filter(
                Q(id__contains=search_val) |
                Q(name__contains=search_val) |
                Q(description__contains=search_val)
            )

        # If advanced search by (e.g. search by a specific field) is provided and advanced search criteria is also provided, then perform advanced search on specific fields
        elif advanced_search_by != '' and advanced_search_criteria != '':

            # Search only by name
            if advanced_search_by == 'name':
                queryset = queryset.filter(Q(name__contains=advanced_search_criteria))
            # Search only by description
            elif advanced_search_by == 'description':
                queryset = queryset.filter(Q(description__contains=advanced_search_criteria))

        #
        # Filter
        #

        # Select List relationships to filter on: (none)

        # Many to Many relationships to filter on:

        # Linguistic Notions
        linguisticnotion = self.request.GET.get('advanced_filter_linguisticnotion', '')
        if linguisticnotion != '':
            queryset = queryset.filter(linguistic_notion__in=[linguisticnotion])

        #
        # Order
        #

        order = self.request.GET.get('advanced_order_direction', '') + self.request.GET.get('advanced_order_by', 'id')
        # If starts with a '-' then it means order descending
        if order[0] == '-':
            queryset = queryset.order_by(Lower(order[1:]).desc())
        else:
            queryset = queryset.order_by(Lower(order))

        #
        # Return data
        #

        return queryset

    def get_context_data(self, **kwargs):
        # Get current context
        context = super(BrowseLinguisticFieldListView, self).get_context_data(**kwargs)
        # Add data for related models
        context['linguisticnotions'] = models.LinguisticNotion.objects.filter(admin_published=True)
        return context
