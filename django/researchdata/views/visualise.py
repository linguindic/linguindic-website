from django.views.generic import (TemplateView)


class VisualiseTemplateView(TemplateView):
    """
    Class-based view to show the visualise template
    """
    template_name = 'researchdata/visualise.html'
