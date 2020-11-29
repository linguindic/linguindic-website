from django.urls import path
from . import views

urlpatterns = [

    # ************
    # Website URLs
    # ************

    # Browse: References
    path('browse/references/', views.BrowseReferenceListView.as_view(), name='browse-references-list'),
    path('browse/references/<pk>/', views.BrowseReferenceDetailView.as_view(), name='browse-references-detail'),

    # Browse: Texts
    path('browse/texts/', views.BrowseTextListView.as_view(), name='browse-texts-list'),
    path('browse/texts/<pk>/', views.BrowseTextDetailView.as_view(), name='browse-texts-detail'),

    # Browse: Author
    path('browse/author/', views.BrowseAuthorListView.as_view(), name='browse-author-list'),
    path('browse/author/<pk>/', views.BrowseAuthorDetailView.as_view(), name='browse-author-detail'),

    # Browse: Linguistic Fields
    path('browse/linguisticfields/', views.BrowseLinguisticFieldListView.as_view(), name='browse-linguisticfields-list'),
    path('browse/linguisticfields/<pk>/', views.BrowseLinguisticFieldDetailView.as_view(), name='browse-linguisticfields-detail'),

    # Browse: Linguistic Notions
    path('browse/linguisticnotions/', views.BrowseLinguisticNotionListView.as_view(), name='browse-linguisticnotions-list'),
    path('browse/linguisticnotions/<pk>/', views.BrowseLinguisticNotionDetailView.as_view(), name='browse-linguisticnotions-detail'),

    # Compare
    path('compare/linguisticnotions/', views.CompareLinguisticNotionsTemplateView.as_view(), name='compare-linguisticnotions'),

    # Visualise
    path('visualise/', views.VisualiseTemplateView.as_view(), name='visualise'),


    # ********
    # API URLs
    # ********

    path('api/', views.APITemplateView.as_view(), name='api'),

    # Select List

    # SlLinguisticNotionsRelationshipType
    path('api/sllinguisticnotionsrelationshiptypes/', views.SlLinguisticNotionsRelationshipTypeListAPIView.as_view(), name='api-sllinguisticnotionsrelationshiptypes-list'),
    path('api/sllinguisticnotionsrelationshiptypes/<pk>/', views.SlLinguisticNotionsRelationshipTypeRetrieveAPIView.as_view(), name='api-sllinguisticnotionsrelationshiptypes-retrieve'),

    # SlLinguisticTraditionGroup
    path('api/sllinguistictraditiongroups/', views.SlLinguisticTraditionGroupListAPIView.as_view(), name='api-sllinguistictraditiongroups-list'),
    path('api/sllinguistictraditiongroups/<pk>/', views.SlLinguisticTraditionGroupRetrieveAPIView.as_view(), name='api-sllinguistictraditiongroups-retrieve'),

    # SlLinguisticTradition
    path('api/sllinguistictraditions/', views.SlLinguisticTraditionListAPIView.as_view(), name='api-sllinguistictraditions-list'),
    path('api/sllinguistictraditions/<pk>/', views.SlLinguisticTraditionRetrieveAPIView.as_view(), name='api-sllinguistictraditions-retrieve'),

    # SlReferencePublisher
    path('api/slreferencepublishers/', views.SlReferencePublisherListAPIView.as_view(), name='api-slreferencepublishers-list'),
    path('api/slreferencepublishers/<pk>/', views.SlReferencePublisherRetrieveAPIView.as_view(), name='api-slreferencepublishers-retrieve'),

    # SlReferenceType
    path('api/slreferencetypes/', views.SlReferenceTypeListAPIView.as_view(), name='api-slreferencetypes-list'),
    path('api/slreferencetypes/<pk>/', views.SlReferenceTypeRetrieveAPIView.as_view(), name='api-slreferencetypes-retrieve'),

    # SlTextGroup
    path('api/sltextgroups/', views.SlTextGroupListAPIView.as_view(), name='api-sltextgroups-list'),
    path('api/sltextgroups/<pk>/', views.SlTextGroupRetrieveAPIView.as_view(), name='api-sltextgroups-retrieve'),

    # SlTextType
    path('api/sltexttypes/', views.SlTextTypeListAPIView.as_view(), name='api-sltexttypes-list'),
    path('api/sltexttypes/<pk>/', views.SlTextTypeRetrieveAPIView.as_view(), name='api-sltexttypes-retrieve'),

    # Main models

    # References
    path('api/references/', views.ReferenceListAPIView.as_view(), name='api-references-list'),
    path('api/references/<pk>/', views.ReferenceRetrieveAPIView.as_view(), name='api-references-retrieve'),

    # Texts
    path('api/texts/', views.TextListAPIView.as_view(), name='api-texts-list'),
    path('api/texts/<pk>/', views.TextRetrieveAPIView.as_view(), name='api-texts-retrieve'),

    # Authors
    path('api/authors/', views.AuthorListAPIView.as_view(), name='api-authors-list'),
    path('api/authors/<pk>/', views.AuthorRetrieveAPIView.as_view(), name='api-authors-retrieve'),

    # LinguisticField
    path('api/linguisticfields/', views.LinguisticFieldListAPIView.as_view(), name='api-linguisticfields-list'),
    path('api/linguisticfields/<pk>/', views.LinguisticFieldRetrieveAPIView.as_view(), name='api-linguisticfields-retrieve'),

    # Linguistic Notions
    path('api/linguisticnotions/', views.LinguisticNotionListAPIView.as_view(), name='api-linguisticnotions-list'),
    path('api/linguisticnotions/<pk>/', views.LinguisticNotionRetrieveAPIView.as_view(), name='api-linguisticnotions-retrieve'),

    # Many to Many models

    # M2MLinguisticNotionsRelationship
    path('api/m2mlinguisticnotionsrelationship/', views.M2MLinguisticNotionsRelationshipListAPIView.as_view(), name='api-m2mlinguisticnotionsrelationship-list'),
    path('api/m2mlinguisticnotionsrelationship/<pk>/', views.M2MLinguisticNotionsRelationshipRetrieveAPIView.as_view(), name='api-m2mlinguisticnotionsrelationship-retrieve'),

]
