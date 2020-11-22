from django.views.generic import TemplateView


class WelcomeTemplateView(TemplateView):
    """
    Welcome-based view to show the welcome template
    """
    template_name = 'general/welcome.html'


class ProjectTemplateView(TemplateView):
    """
    Class-based view to show the project template
    """
    template_name = 'general/project.html'


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
