from django.views.generic import TemplateView


class WelcomeTemplateView(TemplateView):
    """
    Welcome-based view to show the welcome template
    """
    template_name = 'general/welcome.html'


class AboutProjectTemplateView(TemplateView):
    """
    Class-based view to show the project template
    """
    template_name = 'general/about-project.html'


class AboutTeamTemplateView(TemplateView):
    """
    Class-based view to show the team template
    """
    template_name = 'general/about-team.html'


class AboutFundingTemplateView(TemplateView):
    """
    Class-based view to show the funding template
    """
    template_name = 'general/about-funding.html'


class AboutEventsTemplateView(TemplateView):
    """
    Class-based view to show the events template
    """
    template_name = 'general/about-events.html'


class AboutOutputsTemplateView(TemplateView):
    """
    Class-based view to show the outputs template
    """
    template_name = 'general/about-outputs.html'


class CookiesTemplateView(TemplateView):
    """
    Class-based view to show the cookies template
    """
    template_name = 'general/cookies.html'


class AccessibilityTemplateView(TemplateView):
    """
    Class-based view to show the accessiblity template
    """
    template_name = 'general/accessibility.html'
