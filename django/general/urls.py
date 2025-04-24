from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome'),

    path('about/project/', views.AboutProjectTemplateView.as_view(), name='about-project'),
    path('about/database/', views.AboutDatabaseTemplateView.as_view(), name='about-database'),
    path('about/team/', views.AboutTeamTemplateView.as_view(), name='about-team'),
    path('about/funding/', views.AboutFundingTemplateView.as_view(), name='about-funding'),
    path('about/events/', views.AboutEventsTemplateView.as_view(), name='about-events'),
    path('about/outputs/', views.AboutOutputsTemplateView.as_view(), name='about-outputs'),

    path('conference/', views.ConferenceIntroductionTemplateView.as_view(), name='conference-introduction'),
    path('conference/registration/', views.ConferenceRegistrationTemplateView.as_view(), name='conference-registration'),
    path('conference/callforpapers/', views.ConferenceCallForPapersTemplateView.as_view(), name='conference-callforpapers'),
    path('conference/keynotespeakers/', views.ConferenceKeynoteSpeakersTemplateView.as_view(), name='conference-keynotespeakers'),
    path('conference/programme/', views.ConferenceProgrammeTemplateView.as_view(), name='conference-programme'),
    path('conference/accommodation/', views.ConferenceAccommodationTemplateView.as_view(), name='conference-accommodation'),
    path('conference/contact/', views.ConferenceContactTemplateView.as_view(), name='conference-contact'),

    path('help/', views.HelpTemplateView.as_view(), name='help'),
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies'),
    path('accessibility/', views.AccessibilityTemplateView.as_view(), name='accessibility'),
    path('robots.txt', views.RobotsTemplateView.as_view(), name='robots'),
]
