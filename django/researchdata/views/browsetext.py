from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from .. import models
from . import common


class BrowseTextDetailView(DetailView):
    """
    Class-based view to show the text detail template
    """
    template_name = 'researchdata/browse-text-detail.html'
    model = models.Text


class BrowseTextListView(ListView):
    """
    Class-based view to show the text list template
    """
    template_name = 'researchdata/browse-text-list.html'
    model = models.Text
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
                Q(alternative_name__contains=search_val) |
                Q(description__contains=search_val) |
                Q(approximate_date_of_creation__contains=search_val) |
                Q(location__contains=search_val) |
                Q(author_main__contains=search_val)
            )

        # If advanced search by (e.g. search by a specific field) is provided and advanced search criteria is also provided, then perform advanced search on specific fields
        elif advanced_search_by != '' and advanced_search_criteria != '':

            # Search only by name
            if advanced_search_by == 'name':
                queryset = queryset.filter(Q(name__contains=advanced_search_criteria))
            # Search only by alternative name
            elif advanced_search_by == 'alternative_name':
                queryset = queryset.filter(Q(alternative_name__contains=advanced_search_criteria))
            # Search only by description
            elif advanced_search_by == 'description':
                queryset = queryset.filter(Q(description__contains=advanced_search_criteria))
            # Search only by approximate date of creation
            elif advanced_search_by == 'approximate_date_of_creation':
                queryset = queryset.filter(Q(approximate_date_of_creation__contains=advanced_search_criteria))
            # Search only by location
            elif advanced_search_by == 'location':
                queryset = queryset.filter(Q(location__contains=advanced_search_criteria))
            # Search only by main author
            elif advanced_search_by == 'author_main':
                queryset = queryset.filter(Q(author_main__contains=advanced_search_criteria))

        #
        # Filter
        #

        # Many to One relationship filters
        # SL Text Group
        sltextgroup = self.request.GET.get('advanced_filter_sltextgroup', '')
        if sltextgroup != '':
            queryset = queryset.filter(text_group=sltextgroup)
        # SL Text Type
        sltexttype = self.request.GET.get('advanced_filter_sltexttype', '')
        if sltexttype != '':
            queryset = queryset.filter(text_type=sltexttype)

        # One to Many relationship filters
        textpassage = self.request.GET.get('advanced_filter_textpassage', '')
        if textpassage != '':
            queryset = queryset.filter(textpassage=textpassage)

        # Many to Many relationship filters
        queryset = common.filter_queryset_by_m2m(self.request.GET, queryset, 'text')

        # Admin published filter
        queryset = queryset.filter(admin_published=True)

        #
        # Order
        #

        queryset = common.order_queryset(self.request.GET, queryset, 'name')

        #
        # Return data
        #

        return queryset

    def get_context_data(self, **kwargs):
        # Get current view's context
        context = super(BrowseTextListView, self).get_context_data(**kwargs)
        # Add data for related models
        context = common.add_main_models_to_context(context, 'text')
        context['sltextgroups'] = models.SlTextGroup.objects.filter(admin_published=True)
        context['sltexttypes'] = models.SlTextType.objects.filter(admin_published=True)
        # Return context
        return context
