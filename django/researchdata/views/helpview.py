from django.views.generic import (TemplateView)


class HelpTemplateView(TemplateView):
    """
    Class-based view to show the help template
    """
    template_name = 'researchdata/help.html'
