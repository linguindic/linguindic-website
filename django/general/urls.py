from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome'),
    path('project/', views.ProjectTemplateView.as_view(), name='project'),
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies'),
    path('accessibility/', views.AccessibilityTemplateView.as_view(), name='accessibility'),
]
