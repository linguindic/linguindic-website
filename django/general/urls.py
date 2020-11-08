from django.urls import path
from . import views

urlpatterns = [
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies'),
    path('accessibility/', views.AccessibilityTemplateView.as_view(), name='accessibility'),
]
