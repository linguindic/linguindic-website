from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from .. import models
from . import common


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
                Q(title__contains=search_val) |
                Q(subtitle__contains=search_val) |
                Q(authors_list__contains=search_val) |
                Q(editors__contains=search_val) |
                Q(school__contains=search_val) |
                Q(book_title__contains=search_val) |
                Q(journal_title__contains=search_val) |
                Q(volume__contains=search_val) |
                Q(number__contains=search_val) |
                Q(location__contains=search_val) |
                Q(year__contains=search_val) |
                Q(page_start__contains=search_val) |
                Q(page_end__contains=search_val) |
                Q(url__contains=search_val) |
                Q(public_notes__contains=search_val) |
                Q(last_accessed_date__contains=search_val)
            )

        # If advanced search by (e.g. search by a specific field) is provided and advanced search criteria is also provided, then perform advanced search on specific fields
        elif advanced_search_by != '' and advanced_search_criteria != '':

            # Search only by title
            if advanced_search_by == 'title':
                queryset = queryset.filter(Q(title__contains=advanced_search_criteria))
            # Search only by subtitle
            elif advanced_search_by == 'subtitle':
                queryset = queryset.filter(Q(subtitle__contains=advanced_search_criteria))
            # Search only by authors
            elif advanced_search_by == 'authors_list':
                queryset = queryset.filter(Q(authors_list__contains=advanced_search_criteria))
            # Search only by editors
            elif advanced_search_by == 'editors':
                queryset = queryset.filter(Q(editors__contains=advanced_search_criteria))
            # Search only by school
            elif advanced_search_by == 'school':
                queryset = queryset.filter(Q(school__contains=advanced_search_criteria))
            # Search only by book title
            elif advanced_search_by == 'book_title':
                queryset = queryset.filter(Q(book_title__contains=advanced_search_criteria))
            # Search only by journal title
            elif advanced_search_by == 'journal_title':
                queryset = queryset.filter(Q(journal_title__contains=advanced_search_criteria))
            # Search only by volume
            elif advanced_search_by == 'volume':
                queryset = queryset.filter(Q(volume__contains=advanced_search_criteria))
            # Search only by number
            elif advanced_search_by == 'number':
                queryset = queryset.filter(Q(number__contains=advanced_search_criteria))
            # Search only by location
            elif advanced_search_by == 'location':
                queryset = queryset.filter(Q(location__contains=advanced_search_criteria))
            # Search only by year
            elif advanced_search_by == 'year':
                queryset = queryset.filter(Q(year__contains=advanced_search_criteria))
            # Search only by page start
            elif advanced_search_by == 'page_start':
                queryset = queryset.filter(Q(page_start__contains=advanced_search_criteria))
            # Search only by page end
            elif advanced_search_by == 'page_end':
                queryset = queryset.filter(Q(page_end__contains=advanced_search_criteria))
            # Search only by url
            elif advanced_search_by == 'url':
                queryset = queryset.filter(Q(url__contains=advanced_search_criteria))
            # Search only by public_notes
            elif advanced_search_by == 'public_notes':
                queryset = queryset.filter(Q(public_notes__contains=advanced_search_criteria))
            # Search only by last accessed date
            elif advanced_search_by == 'last_accessed_date':
                queryset = queryset.filter(Q(last_accessed_date__contains=advanced_search_criteria))

        #
        # Filter
        #

        # Many to One relationship filters
        # SL Reference Type
        slreferencetype = self.request.GET.get('advanced_filter_slreferencetype', '')
        if slreferencetype != '':
            queryset = queryset.filter(reference_type=slreferencetype)
        # SL Reference Publisher
        slreferencepublisher = self.request.GET.get('advanced_filter_slreferencepublisher', '')
        if slreferencepublisher != '':
            queryset = queryset.filter(reference_publisher=slreferencepublisher)

        # Many to Many relationship filters
        queryset = common.filter_queryset_by_m2m(self.request.GET, queryset, 'linguisticfield')

        # Admin published filter
        queryset = queryset.filter(admin_published=True)

        #
        # Order
        #

        queryset = common.order_queryset(self.request.GET, queryset, 'title')

        #
        # Return data
        #

        return queryset

    def get_context_data(self, **kwargs):
        # Get current view's context
        context = super(BrowseReferenceListView, self).get_context_data(**kwargs)
        # Add data for related models
        context = common.add_main_models_to_context(context, 'linguisticfield')
        context['slreferencetypes'] = models.SlReferenceType.objects.filter(admin_published=True)
        context['slreferencepublishers'] = models.SlReferencePublisher.objects.filter(admin_published=True)
        # Return context
        return context
