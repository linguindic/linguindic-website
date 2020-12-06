from django.views.generic import TemplateView


class WelcomeTemplateView(TemplateView):
    """
    Welcome-based view to show the welcome template
    """
    template_name = 'general/welcome.html'


class ProjectAboutTemplateView(TemplateView):
    """
    Class-based view to show the project about template
    """
    template_name = 'general/project-about.html'


class ProjectTeamTemplateView(TemplateView):
    """
    Class-based view to show the project team template
    """
    template_name = 'general/project-team.html'


class ProjectFundingTemplateView(TemplateView):
    """
    Class-based view to show the project funding template
    """
    template_name = 'general/project-funding.html'


class ProjectEventsTemplateView(TemplateView):
    """
    Class-based view to show the project events template
    """
    template_name = 'general/project-events.html'


class ProjectOutputsTemplateView(TemplateView):
    """
    Class-based view to show the project outputs template
    """
    template_name = 'general/project-outputs.html'


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
