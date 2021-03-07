from django.db.models.functions import Lower
from .. import models


def filter_queryset_by_m2m(request, queryset, exclude):
    """
    request = e.g. self.request.GET
    queryset = a Django queryset object
    exclude = e.g. 'linguisticfield' if want to exclude filter on LinguisticField

    Returns an appropriately filtered Django queryset object
    """

    # request and queryset are mandatory
    if request is not None and queryset is not None:

        if exclude != 'author':
            author = request.get('advanced_filter_author', '')
            if author != '':
                queryset = queryset.filter(author__in=[author])

        if exclude != 'linguisticfield':
            linguisticfield = request.get('advanced_filter_linguisticfield', '')
            if linguisticfield != '':
                queryset = queryset.filter(linguisticfield__in=[linguisticfield])

        if exclude != 'linguisticnotion':
            linguisticnotion = request.get('advanced_filter_linguisticnotion', '')
            if linguisticnotion != '':
                queryset = queryset.filter(linguisticnotion__in=[linguisticnotion])

        if exclude != 'linguistictradition':
            linguistictradition = request.get('advanced_filter_linguistictradition', '')
            if linguistictradition != '':
                queryset = queryset.filter(linguistictradition__in=[linguistictradition])

        if exclude != 'reference':
            reference = request.get('advanced_filter_reference', '')
            if reference != '':
                queryset = queryset.filter(reference__in=[reference])

        if exclude != 'sanskritword':
            sanskritword = request.get('advanced_filter_sanskritword', '')
            if sanskritword != '':
                queryset = queryset.filter(sanskritword__in=[sanskritword])

        if exclude != 'text':
            text = request.get('advanced_filter_text', '')
            if text != '':
                queryset = queryset.filter(text__in=[text])

        if exclude != 'textpassage':
            textpassage = request.get('advanced_filter_textpassage', '')
            if textpassage != '':
                queryset = queryset.filter(textpassage__in=[textpassage])

    # Only show results that admin approves as published
    return queryset.filter(admin_published=True)


def order_queryset(request, queryset, order_by_default):
    """
    request = http request object, e.g. self.request.GET
    queryset = a Django queryset object
    order_by_default = default field to order by, e.g. name, last_name, id, ...

    Returns an ordered Django queryset object
    """
    
    # request and queryset are mandatory
    if request is not None and queryset is not None:

        # If no order_by_default given, then set to 'id'
        if order_by_default is None:
            order_by_default = 'last_name'

        # Establish the order direction (asc/desc) and the field to order by, from the request
        
        order = request.get('advanced_order_direction', '') + request.get('advanced_order_by', order_by_default)

        # If starts with a '-' then it means order descending
        if order[0] == '-':
            queryset = queryset.order_by(Lower(order[1:]).desc())
        else:
            queryset = queryset.order_by(Lower(order))

    return queryset


def add_main_models_to_context(context, exclude):
    """
    context = a context data dictionary, e.g. super(ExampleListView, self).get_context_data(**kwargs)
    exclude = e.g. 'linguisticfield' if want to exclude returning LinguisticField objects

    Returns a context dictionary
    """

    # context is mandatory
    if context is not None:

        if exclude != 'author':
            context['authors'] = models.Author.objects.filter(admin_published=True)

        if exclude != 'linguisticfield':
            context['linguisticfields'] = models.LinguisticField.objects.filter(admin_published=True)

        if exclude != 'linguisticnotion':
            context['linguisticnotions'] = models.LinguisticNotion.objects.filter(admin_published=True)

        if exclude != 'linguistictradition':
            context['linguistictraditions'] = models.LinguisticTradition.objects.filter(admin_published=True)

        if exclude != 'reference':
            context['references'] = models.Reference.objects.filter(admin_published=True)

        if exclude != 'sanskritword':
            context['sanskritwords'] = models.SanskritWord.objects.filter(admin_published=True)

        if exclude != 'text':
            context['texts'] = models.Text.objects.filter(admin_published=True)

        if exclude != 'textpassage':
            context['textpassages'] = models.TextPassage.objects.filter(admin_published=True)

        return context
