from django.views.generic import (TemplateView)


class CompareLinguisticNotionsTemplateView(TemplateView):
    """
    Class-based view to show the compare linguistic notions template
    """
    template_name = 'researchdata/compare-linguisticnotions.html'
