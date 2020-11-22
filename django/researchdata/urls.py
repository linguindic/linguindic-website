from django.urls import path
from . import views

urlpatterns = [

    # Website URLs

    # Linguistic Notions
    path('linguisticnotions/', views.LinguisticNotionListView.as_view(), name='linguisticnotions-list'),
    path('linguisticnotions/<pk>/', views.LinguisticNotionDetailView.as_view(), name='linguisticnotions-detail'),


    # API URLs

    # Linguistic Notions
    path('api/', views.APITemplateView.as_view(), name='api'),
    path('api/linguisticnotions/', views.LinguisticNotionListAPIView.as_view(), name='api-linguisticnotions-list'),
    path('api/linguisticnotions/<pk>/', views.LinguisticNotionRetrieveAPIView.as_view(), name='api-linguisticnotions-retrieve')
]
