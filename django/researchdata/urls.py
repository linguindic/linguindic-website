from django.urls import path
from .views import (
    api,
    browseauthor,
    browselinguisticfield,
    browselinguisticnotion,
    browselinguistictradition,
    browsereference,
    browsesanskritword,
    browsetext,
    browsetextpassage,
    compare,
    visualise
)

urlpatterns = [

    # ************
    # Website URLs
    # ************

    # Browse: Author
    path('browse/authors/', browseauthor.BrowseAuthorListView.as_view(), name='browse-authors-list'),
    path('browse/authors/<pk>/', browseauthor.BrowseAuthorDetailView.as_view(), name='browse-authors-detail'),

    # Browse: Linguistic Fields
    path('browse/linguisticfields/', browselinguisticfield.BrowseLinguisticFieldListView.as_view(), name='browse-linguisticfields-list'),
    path('browse/linguisticfields/<pk>/', browselinguisticfield.BrowseLinguisticFieldDetailView.as_view(), name='browse-linguisticfields-detail'),

    # Browse: Linguistic Notions
    path('browse/linguisticnotions/', browselinguisticnotion.BrowseLinguisticNotionListView.as_view(), name='browse-linguisticnotions-list'),
    path('browse/linguisticnotions/<pk>/', browselinguisticnotion.BrowseLinguisticNotionDetailView.as_view(), name='browse-linguisticnotions-detail'),

    # Browse: Linguistic Traditions
    path('browse/linguistictraditions/', browselinguistictradition.BrowseLinguisticTraditionListView.as_view(), name='browse-linguistictraditions-list'),
    path('browse/linguistictraditions/<pk>/', browselinguistictradition.BrowseLinguisticTraditionDetailView.as_view(), name='browse-linguistictraditions-detail'),

    # Browse: References
    path('browse/references/', browsereference.BrowseReferenceListView.as_view(), name='browse-references-list'),
    path('browse/references/<pk>/', browsereference.BrowseReferenceDetailView.as_view(), name='browse-references-detail'),

    # Browse: Sanskrit Words
    path('browse/sanskritwords/', browsesanskritword.BrowseSanskritWordListView.as_view(), name='browse-sanskritwords-list'),
    path('browse/sanskritwords/<pk>/', browsesanskritword.BrowseSanskritWordDetailView.as_view(), name='browse-sanskritwords-detail'),

    # Browse: Texts
    path('browse/texts/', browsetext.BrowseTextListView.as_view(), name='browse-texts-list'),
    path('browse/texts/<pk>/', browsetext.BrowseTextDetailView.as_view(), name='browse-texts-detail'),

    # Browse: Text Passages
    path('browse/textpassages/', browsetextpassage.BrowseTextPassageListView.as_view(), name='browse-textpassages-list'),
    path('browse/textpassages/<pk>/', browsetextpassage.BrowseTextPassageDetailView.as_view(), name='browse-textpassages-detail'),

    # Compare
    path('compare/linguisticnotions/', compare.CompareLinguisticNotionsTemplateView.as_view(), name='compare-linguisticnotions'),

    # Visualise
    path('visualise/', visualise.VisualiseTemplateView.as_view(), name='visualise'),


    # ********
    # API URLs
    # ********

    path('api/', api.APITemplateView.as_view(), name='api'),

    # Select List

    # SlLinguisticTraditionGroup
    path('api/sllinguistictraditiongroups/', api.SlLinguisticTraditionGroupListAPIView.as_view(), name='api-sllinguistictraditiongroups-list'),
    path('api/sllinguistictraditiongroups/<pk>/', api.SlLinguisticTraditionGroupRetrieveAPIView.as_view(), name='api-sllinguistictraditiongroups-retrieve'),

    # SlReferencePublisher
    path('api/slreferencepublishers/', api.SlReferencePublisherListAPIView.as_view(), name='api-slreferencepublishers-list'),
    path('api/slreferencepublishers/<pk>/', api.SlReferencePublisherRetrieveAPIView.as_view(), name='api-slreferencepublishers-retrieve'),

    # SlReferenceType
    path('api/slreferencetypes/', api.SlReferenceTypeListAPIView.as_view(), name='api-slreferencetypes-list'),
    path('api/slreferencetypes/<pk>/', api.SlReferenceTypeRetrieveAPIView.as_view(), name='api-slreferencetypes-retrieve'),

    # SlTextGroup
    path('api/sltextgroups/', api.SlTextGroupListAPIView.as_view(), name='api-sltextgroups-list'),
    path('api/sltextgroups/<pk>/', api.SlTextGroupRetrieveAPIView.as_view(), name='api-sltextgroups-retrieve'),

    # SlTextType
    path('api/sltexttypes/', api.SlTextTypeListAPIView.as_view(), name='api-sltexttypes-list'),
    path('api/sltexttypes/<pk>/', api.SlTextTypeRetrieveAPIView.as_view(), name='api-sltexttypes-retrieve'),

    # Main models

    # Authors
    path('api/authors/', api.AuthorListAPIView.as_view(), name='api-authors-list'),
    path('api/authors/<pk>/', api.AuthorRetrieveAPIView.as_view(), name='api-authors-retrieve'),

    # Linguistic Fields
    path('api/linguisticfields/', api.LinguisticFieldListAPIView.as_view(), name='api-linguisticfields-list'),
    path('api/linguisticfields/<pk>/', api.LinguisticFieldRetrieveAPIView.as_view(), name='api-linguisticfields-retrieve'),

    # Linguistic Notions
    path('api/linguisticnotions/', api.LinguisticNotionListAPIView.as_view(), name='api-linguisticnotions-list'),
    path('api/linguisticnotions/<pk>/', api.LinguisticNotionRetrieveAPIView.as_view(), name='api-linguisticnotions-retrieve'),

    # Linguistic Traditions
    path('api/linguistictraditions/', api.LinguisticTraditionListAPIView.as_view(), name='api-linguistictraditions-list'),
    path('api/linguistictraditions/<pk>/', api.LinguisticTraditionRetrieveAPIView.as_view(), name='api-linguistictraditions-retrieve'),

    # References
    path('api/references/', api.ReferenceListAPIView.as_view(), name='api-references-list'),
    path('api/references/<pk>/', api.ReferenceRetrieveAPIView.as_view(), name='api-references-retrieve'),

    # Sanskrit Words
    path('api/sanskritwords/', api.SanskritWordListAPIView.as_view(), name='api-sanskritwords-list'),
    path('api/sanskritwords/<pk>/', api.SanskritWordRetrieveAPIView.as_view(), name='api-sanskritwords-retrieve'),

    # Texts
    path('api/texts/', api.TextListAPIView.as_view(), name='api-texts-list'),
    path('api/texts/<pk>/', api.TextRetrieveAPIView.as_view(), name='api-texts-retrieve'),

    # Text Passages
    path('api/textpassages/', api.TextPassageListAPIView.as_view(), name='api-textpassages-list'),
    path('api/textpassages/<pk>/', api.TextPassageRetrieveAPIView.as_view(), name='api-textpassages-retrieve')

]
