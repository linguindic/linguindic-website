from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome'),
    path('project/about/', views.ProjectAboutTemplateView.as_view(), name='project-about'),
    path('project/team/', views.ProjectTeamTemplateView.as_view(), name='project-team'),
    path('project/funding/', views.ProjectFundingTemplateView.as_view(), name='project-funding'),
    path('project/events/', views.ProjectEventsTemplateView.as_view(), name='project-events'),
    path('project/outputs/', views.ProjectOutputsTemplateView.as_view(), name='project-outputs'),
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies'),
    path('accessibility/', views.AccessibilityTemplateView.as_view(), name='accessibility'),
]
