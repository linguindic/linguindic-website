from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from django.db.models.functions import Lower
from .. import models


class BrowseAuthorDetailView(DetailView):
    """
    Class-based view to show the author detail template
    """
    template_name = 'researchdata/browse-author-detail.html'
    model = models.Author


class BrowseAuthorListView(ListView):
    """
    Class-based view to show the author list template
    """
    template_name = 'researchdata/browse-author-list.html'
    model = models.Author
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
                Q(first_name__contains=search_val) |
                Q(last_name__contains=search_val) |
                Q(alternative_name__contains=search_val) |
                Q(location_most_active__contains=search_val) |
                Q(date_of_birth__contains=search_val) |
                Q(date_of_death__contains=search_val)
            )

        # If advanced search by (e.g. search by a specific field) is provided and advanced search criteria is also provided, then perform advanced search on specific fields
        elif advanced_search_by != '' and advanced_search_criteria != '':

            # Search only by first name
            if advanced_search_by == 'first_name':
                queryset = queryset.filter(Q(first_name__contains=advanced_search_criteria))
            # Search only by last name
            elif advanced_search_by == 'last_name':
                queryset = queryset.filter(Q(last_name__contains=advanced_search_criteria))
            # Search only by alternative name
            elif advanced_search_by == 'alternative_name':
                queryset = queryset.filter(Q(alternative_name__contains=advanced_search_criteria))
            # Search only by description
            elif advanced_search_by == 'description':
                queryset = queryset.filter(Q(description__contains=advanced_search_criteria))
            # Search only by location most active
            elif advanced_search_by == 'location_most_active':
                queryset = queryset.filter(Q(location_most_active__contains=advanced_search_criteria))
            # Search only by date of birth
            elif advanced_search_by == 'date_of_birth':
                queryset = queryset.filter(Q(date_of_birth__contains=advanced_search_criteria))
            # Search only by date of death
            elif advanced_search_by == 'date_of_death':
                queryset = queryset.filter(Q(date_of_death__contains=advanced_search_criteria))

        #
        # Filter
        #

        # Select List relationships to filter on:

        # SL Linguistic Tradition
        sllinguistictradition = self.request.GET.get('advanced_filter_sllinguistictradition', '')
        if sllinguistictradition != '':
            queryset = queryset.filter(linguistic_tradition=sllinguistictradition)

        # Many to Many relationships to filter on:

        # Linguistic Notions
        linguisticnotion = self.request.GET.get('advanced_filter_linguisticnotion', '')
        if linguisticnotion != '':
            queryset = queryset.filter(linguistic_notion__in=[linguisticnotion])

        # Reference
        reference = self.request.GET.get('advanced_filter_reference', '')
        if reference != '':
            queryset = queryset.filter(reference__in=[reference])

        # Text
        text = self.request.GET.get('advanced_filter_text', '')
        if text != '':
            queryset = queryset.filter(text__in=[text])

        # Only show results that admin approves as published
        queryset = queryset.filter(admin_published=True)

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
        context = super(BrowseAuthorListView, self).get_context_data(**kwargs)
        # Add data for related models
        context['sllinguistictraditions'] = models.SlLinguisticTradition.objects.filter(admin_published=True)
        context['linguisticnotions'] = models.LinguisticNotion.objects.filter(admin_published=True)
        context['references'] = models.Reference.objects.filter(admin_published=True)
        context['texts'] = models.Text.objects.filter(admin_published=True)
        return context
